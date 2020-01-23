import json

from web3 import Web3
from solc import compile_standard

#Lectura del contrato inteligente escrito en Solidity
f = open ('PeopleContract.sol','r')
contractFile = f.read()
f.close()

#Compilación del contrato
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources":{ 
        "PeopleContract.sol":{
            "content": contractFile
        }
    },
    "settings":{
        "outputSelection":{
            "*": {
                "*": ["metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
            }
        }
    }
})

#Obtención del bytecode del contrato
bytecode = compiled_sol['contracts']['PeopleContract.sol']['PeopleContract']['evm']['bytecode']['object']
f = open ('PeopleContract.bytecode','w')
f.write(bytecode)
f.close()

#Obtención del abi del contrato
abi = json.loads(compiled_sol['contracts']['PeopleContract.sol']['PeopleContract']['metadata'])['output']['abi']
textAbi = json.dumps(abi)
f = open ('PeopleContract.abi','w')
f.write(textAbi)
f.close()

#Conexión a la red
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
w3.eth.defaultAccount = w3.eth.accounts[0]

#Intancia del contrato
PeopleContract = w3.eth.contract(abi=abi, bytecode=bytecode)

#Despliegue del contrato
tx_hash = PeopleContract.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Contract Address: ", tx_receipt.contractAddress)




