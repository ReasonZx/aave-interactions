from scripts.helpfulScripts import getAccount
from brownie import config, network, interface

def getWeth():
    account = getAccount()
    weth = interface.IWeth(config["networks"][network.show_active()]["wethToken"])
    tx = weth.deposit({"from": account, "value": 0.01 * 10 ** 18})
    tx.wait(1)
    print("Received 0.01 WETH")
    return tx


def main():
    getWeth()