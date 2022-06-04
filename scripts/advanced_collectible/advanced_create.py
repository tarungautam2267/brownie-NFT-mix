from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_account
from web3 import Web3

def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    print(advanced_collectible)
    tx = advanced_collectible.createCollectible({"from":account})
    tx.wait(1)
    print("Collectible Created!!!")