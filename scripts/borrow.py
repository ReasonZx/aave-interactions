from scripts.helpfulScripts import getAccount, approveERC20
from scripts.getWeth import getWeth
from brownie import config, network, interface
from web3 import Web3

def depositERC20(lendingPool, ERC20adress, amount, account):
    tx = lendingPool.deposit(ERC20adress, Web3.toWei(0.1, "ether"), account.address, 0, {"from" : account})
    tx.wait(1)
    print("Deposited!")
    return tx

def borrowERC20(lendingPool, tokenAdress, amount, borrowType, account):
    tx = lendingPool.borrow(tokenAdress, amount, borrowType, 0 , account.address, {"from" : account})
    tx.wait(1)
    erc20 = interface.IERC20(tokenAdress)
    print("Borrowed " + str(amount) + " " + erc20.symbol())
    return tx

def repayERC20(lendingPool, tokenAdress, amount, account):
    if(amount == 'max'):
        tx = lendingPool.repay(tokenAdress, type(uint256).max, borrowType, account.address, {"from" : account})
        tx.wait(1)
    else:
        tx = lendingPool.repay(tokenAdress, amount, borrowType, account.address, {"from" : account})
        tx.wait(1)

def getLendingPool():
    lendingPoolAdressesProvider = interface.ILendingPoolAddressesProvider(config["networks"][network.show_active()]["lendingPoolAdressesProvider"])
    lendingPoolAdress = lendingPoolAdressesProvider.getLendingPool()

    lendingPool = interface.ILendingPool(lendingPoolAdress)
    return lendingPool

def getAccBorrowData(lendingPool, account):
    (totalCollateralETH, totalDebtETH, availableBorrowsETH, currentLiquidationThreshold, ltv, healthFactor) = lendingPool.getUserAccountData(account.address)
    totalCollateralETH = Web3.fromWei(totalCollateralETH, "ether")
    totalDebtETH = Web3.fromWei(totalDebtETH, "ether")
    availableBorrowsETH = Web3.fromWei(availableBorrowsETH, "ether")
    currentLiquidationThreshold = Web3.fromWei(currentLiquidationThreshold, "ether")
    ltv = Web3.fromWei(ltv, "ether")
    healthFactor = Web3.fromWei(healthFactor, "ether")
    
    print("Eth Collateral: " + str(totalCollateralETH))
    print("Eth Debt: " + str(totalDebtETH))
    print("Eth available to borrow: " + str(availableBorrowsETH))
    print("Ltv: " + str(ltv))
    print("Health factor: " + str(healthFactor))
    return (totalCollateralETH, totalDebtETH, str(availableBorrowsETH))

def getAssetPrice(priceFeedAddress):
    daiEthPriceFeed = interface.AggregatorV3Interface(priceFeedAddress)
    latestPrice = daiEthPriceFeed.latestRoundData()[1]
    latestPrice = Web3.fromWei(latestPrice, "ether")
    print("The DAI/ETH price is "+ str(latestPrice))
    return float(latestPrice)

def main():
    account = getAccount()
    wethAddress = config["networks"][network.show_active()]["wethToken"]
    if ("fork" in network.show_active()):
        getWeth()
    lendingPool = getLendingPool()

    approveERC20(Web3.toWei(0.1, "ether"), lendingPool.address, wethAddress, account)
    
    depositERC20(lendingPool, wethAddress, Web3.toWei(0.1, "ether"), account)

    (totalCollateralETH, totalDebtETH, availableBorrowsETH) = getAccBorrowData(lendingPool, account)

    daiEthPrice = getAssetPrice(config["networks"][network.show_active()]["daiEthPriceFeed"])

    borrowERC20(lendingPool, config["networks"][network.show_active()]["daiToken"],  0.05/ daiEthPrice , 1, account)
    
    getAccBorrowData(lendingPool, account)

    repayERC20(lendingPool, config["networks"][network.show_active()]["daiToken"], 'max', account)


    

    
    