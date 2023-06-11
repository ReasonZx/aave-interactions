from scripts.helpfulScripts import getAccount
from brownie import config, network, interface
from web3 import Web3

def getWeth(amount):
    account = getAccount()
    weth = interface.IWeth(config["networks"][network.show_active()]["wethToken"])
    tx = weth.deposit({"from": account, "value": Web3.toWei(amount, "ether")})
    tx.wait(1)
    print("Received " + str(amount) + " WETH")
    return tx


def main():
    getWeth(0.1)