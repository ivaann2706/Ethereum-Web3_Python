# Ethereum-Web3_Python
Interacción con un contrato inteligente usando python a través de la librería Web3.py

Para la realización de este ejercicio se han usado las siguientes versiones:
- python 3.6.9
- pip 20.0.1
- web3 5.4.0
- py-solc 3.2.0

## Preparación del entorno
Lo primero que se debería hacer es instalar python si aún no se tiene.
```
sudo apt install python3
```

Es recomendable trabajar con entornos virtuales para mantener la configuración de python aislada en cada proyecto. Para ello se instala python3-venv
```
apt-get install python3-venv
```

Una vez instalado la herramienta para trabajar con entornos virtuales, se crea uno de la siguiente manera.
```
python3 -m venv myvenv
```

Para iniciar el entorno virtual se ejecuta el siguiente comando
```
source myvenv/bin/activate
```

Una vez iniciado el entorno virtual se instala el sistema de gestión de paquetes pip
```
python -m pip install --upgrade pip
```

A continuación se usa pip para instalar la librería web3
```
pip install web3
```

En mi caso, al ejecutar el comando anterior salió un error. Para solucionarlo lanzar la siguiente línea de comando.
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev python3.6 python3.6-venv python3.6-dev
```
Para compilar el contrato es necesario instalar la librería py-solc.
```
python pip install py-solc
```

Se utilizará Ganache como red blockchain de prueba.

## Desarrollo y despliegue del contrato

El contrato pensado para este ejemplo es el siguiente.

```
pragma solidity ^0.6.1;

contract PeopleContract {
    Person[] public people;
    
    uint256 peopleCount;
    
    struct Person {
        string _firstName;
        string _lastName;
    }
    
    function addPerson(string memory _firstName, string memory _lastName) public {
        people.push(Person(_firstName, _lastName));
        peopleCount += 1;
    }
    
    function getPeopleCount()public view returns(uint256){
        return peopleCount;
    } 
    
    function getPerson(uint256 index) view public  returns (string memory, string memory){
        return (people[index]._firstName, people[index]._lastName);
    }
}

```

A continuación se desplegará el contrato en la red de Ganache usando Web3. Para ello ejecutamos el siguiente archivo llamado deployContract.py.

```python
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
``` 

El código anterior se puede resumir en:
- Lectura del contrato inteligente escrito en Solidity
- Compilación del contrato
- Obtención del bytecode y abi del contrato
- Conexión a la red
- Instancia del contrato
- Despliegue del contrato

Una vez que el contrato se ha desplegado en la red, obtenemos la dirección del contrato. Esta dirección la necesitaremos para interactuar con él.

Con el siguiente script se pueden realizar llamadas al contrato.

```python
import json
from web3 import Web3

url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(url))

abi = [{"inputs": [{"internalType": "string", "name": "_firstName", "type": "string"}, {"internalType": "string", "name": "_lastName", "type": "string"}], "name": "addPerson", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "getPeopleCount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "getPerson", "outputs": [{"internalType": "string", "name": "", "type": "string"}, {"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "people", "outputs": [{"internalType": "string", "name": "_firstName", "type": "string"}, {"internalType": "string", "name": "_lastName", "type": "string"}], "stateMutability": "view", "type": "function"}]

contractDeployed = w3.eth.contract(address="0xdaDA9fE52cE61bF099Cfd8E9182F6cE154A6B192", abi=abi)

w3.eth.defaultAccount = w3.eth.accounts[0]

tx_hash = contractDeployed.functions.addPerson("ivan","alba").transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

tx_hash = contractDeployed.functions.addPerson("jose","gomez").transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

peopleCount = contractDeployed.functions.getPeopleCount().call()
print(peopleCount)

person = contractDeployed.functions.getPerson(0).call()
print(person)

```
Se necesitan 3 cosas:
- url de un nodo que nos da acceso a la red de pruebas
- abi del contrato inteligente
- dirección del contrato inteligente

Una vez que se tiene una instancia del contrato inteligente, se pueden lanzar las funciones públicas definidas en dicho contrato.