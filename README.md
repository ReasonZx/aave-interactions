# aave-interactions

This project is not working on Sepolia testnet. Use mainnet fork.
Works only with Aave v2


## Testnet
Aave v2 "not supported" on Sepolia Testnet and goerli is not usable anymore.

## Mainnet-fork
To have locally a mainnet-fork go to alchemy.com and create a new app (creates a fork). Then run the following command to add that fork to your local enviroment with brownie:
```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/********* accounts=10 mnemonic=******* port=8545
```

To run the complete script to borrow and repay DAI:
```
brownie run scripts/borrow.py --network mainnet-fork
```