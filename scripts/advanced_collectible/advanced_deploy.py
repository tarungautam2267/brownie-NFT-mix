from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract
from brownie import AdvancedCollectible, network, config
from web3 import Web3
sample_token_uri = "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account})
    
    fund_with_link(advanced_collectible.address)
    tx = advanced_collectible.createCollectible({"from":account})
    tx.wait(1)
    print("Collectible Createdd!!!")


def fund_with_link(contracttofund, amount=Web3.toWei(5,"ether")):
    print("Funding contract with Link Tokens...")
    account = get_account()
    link_token = get_contract("link_token")
    tx = link_token.transfer(contracttofund, amount,{"from":account})
    tx.wait(1)
    print("Contract funded with Link Tokens!!!")


def main():
    deploy_and_create()