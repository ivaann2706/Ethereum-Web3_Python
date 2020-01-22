import json
from web3 import Web3

url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

abi = [{"inputs":[{"internalType":"string","name":"_saludo","type":"string"}],"name":"modificarSaludo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"saludar","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"saludo","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"}]

contract = web3.eth.contract(address="0x3e0385258Cd7F07C69308EEd1E0DE9dd84214F4B", abi=abi)

saludo = contract.functions.saludar().call()
print(saludo)

web3.eth.defaultAccount = "0x78784cC124Dc8c855e68D88F1F65b28C4A2cF839"

tx_hash = contract.functions.modificarSaludo("hola").transact()
web3.eth.waitForTransactionReceipt(tx_hash)

#contract.functions.modificarSaludo("adios").transact({'from': '0x78784cC124Dc8c855e68D88F1F65b28C4A2cF839'})

saludo = contract.functions.saludar().call()
print(saludo)
