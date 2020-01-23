import json
from web3 import Web3

url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(url))

abi = [{"inputs": [{"internalType": "string", "name": "_firstName", "type": "string"}, {"internalType": "string", "name": "_lastName", "type": "string"}], "name": "addPerson", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "getPeopleCount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "getPerson", "outputs": [{"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "people", "outputs": [{"internalType": "string", "name": "_firstName", "type": "string"}, {"internalType": "string", "name": "_lastName", "type": "string"}], "stateMutability": "view", "type": "function"}]

contractDeployed = w3.eth.contract(address="0xd4BD80FF53ac800266a4CCabD0C3720e82f50991", abi=abi)

w3.eth.defaultAccount = w3.eth.accounts[0]

tx_hash = contractDeployed.functions.addPerson("ivan","alba").transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

tx_hash = contractDeployed.functions.addPerson("jose","gomez").transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

peopleCount = contractDeployed.functions.getPeopleCount().call()
print(peopleCount)

person = contractDeployed.functions.getPerson(0).call()
print(person)