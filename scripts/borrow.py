from scripts.helpfulScripts import getAccount, approveERC20
from scripts.getWeth import getWeth
from brownie import config, network, interface
from web3 import Web3

def borrow(_account):
    print("Naad")

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


def main():
    account = getAccount()
    wethAddress = config["networks"][network.show_active()]["wethToken"]
    if ("fork" in network.show_active()):
        getWeth()
    lendingPool = getLendingPool()

    approveERC20(Web3.toWei(0.1, "ether"), lendingPool.address, wethAddress, account)
    
    tx = lendingPool.deposit(wethAddress, Web3.toWei(0.1, "ether"), account.address, 0, {"from" : account})
    tx.wait(1)
    print("Deposited!")


    (totalCollateralETH, totalDebtETH, availableBorrowsETH) = getAccBorrowData(lendingPool, account)


    

    
    