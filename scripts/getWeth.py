from scripts.helpfulScripts import getAccount
from brownie import config, network, interface
from web3 import Web3

def getWeth():
    account = getAccount()
    weth = interface.IWeth(config["networks"][network.show_active()]["wethToken"])
    tx = weth.deposit({"from": account, "value": Web3.toWei(0.2, "ether")})
    tx.wait(1)
    print("Received 0.02 WETH")
    return tx


def main():
    getWeth()