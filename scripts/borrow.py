from scripts.helpfulScripts import getAccount
from scripts.getWeth import getWeth
from brownie import config, network, interface


def borrow(_account):
    print("Naad")

def getLendingPool():
    lendingPoolAdressesProvider = interface.ILendingPoolAddressesProvider(config["networks"][network.show_active()]["lendingPoolAdressesProvider"])
    lendingPoolAdress = lendingPoolAdressesProvider.getLendingPool()

    lendingPool = interface.ILendingPool(lendingPoolAdress)
    return lendingPool


def main():
    account = getAccount()
    if ("fork" in network.show_active()):
        getWeth()
    lendingPool = getLendingPool()
    print(lendingPool)
    
    