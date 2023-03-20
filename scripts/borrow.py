from scripts.helpfulScripts import getAccount
from scripts.getWeth import getWeth
from brownie import config, network, interface



def main():
    account = getAccount()