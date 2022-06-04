from brownie import network, config, accounts, Contract, LinkToken, VRFCoordinatorMock
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local", "mainnet-fork", "mainnet-fork-dev"]
DECIMALS = 8
STARTING_PRICE = 200000000000
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


contracts_to_mock={ "link_token": LinkToken,"vrf_coordinator": VRFCoordinatorMock}

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT):
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print("Deploying Link Token..")
    link_token=LinkToken.deploy({"from":get_account()})
    print("Depoying VRFCoordinator...")
    VRFCoordinatorMock.deploy(link_token.address,{"from":get_account()})

def get_contract(contract_name):
    contract_type = contracts_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        if len(contract_type)<=0:
            print("Deploying Mocks...")
            deploy_mocks()
            print("Mocks Deployed!!")
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(f"{contract_type}", contract_address, contract_type.abi)
    return contract