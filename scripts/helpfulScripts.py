from brownie import (accounts, network, config, Contract)

# contractList = {
#     "link": LinkToken
# }

def getAccount():
    if network.show_active() == "development" or ("fork" in network.show_active()):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def getContractAddress(_contractName, _account=None):
    if network.show_active() == "development":
        mockAggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": _account})
        return mockAggregator.address
    else:
        return config["networks"][network.show_active()][_contractName]

def getContract(_contractName, _account=None):
    SCaddress = getContractAddress(_contractName, _account)
    if network.show_active() == "development":
        print("Functionality not available in development network. Use testnet or local fork.")
        exit()
    elif(_contractName not in contractList):
        print("Using LINK as default Token to fund contract")
        contract = Contract.from_abi(LinkToken.name, SCaddress, LinkToken.abi)
    else:
        contract = Contract.from_abi(contractList[_contractName]._name, SCaddress, contractList[_contractName].abi)
    
    return contract 



# def fundSC (_SCadress, _account=None, _tokenName=None, _ammount = 100000000000000000):      #0.1
#     if(not _account):
#         _account = getAccount()

#     if((not _tokenName) or (_tokenName not in contractList)):
#         print("Using LINK as default Token to fund contract")
#         tokenSC = getContract("link")
#     else :
#         tokenSC = getContract(contractList(lower(_tokenName)))

#     tx = tokenSC.transfer(_SCadress, _ammount, {"from": _account})
#     tx.wait(1)
    
#     print("Contracted funded!")
#     return tx