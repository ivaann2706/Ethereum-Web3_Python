# Ethereum-Web3_Python
Interacción con un contrato inteligente usando python a través de la librería Web3.py

Para la realización de este ejercicio se han usado las siguientes versiones:
- python 3.6.9
- pip 20.0.1
- web3 5.4.0

## Preparación del entorno
Lo  primero que se debería hacer es instalar python si aún no se tiene.
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
}
```
El siguiente contrato también se ha probado.
```
pragma solidity ^0.6.1;

contract Saludador {
    string public saludo;
    
    constructor() public {
        saludo = 'Hello!';
    }
    
    function modificarSaludo(string memory _saludo) public {
        saludo = _saludo;
    }
    
    function saludar() view public returns (string memory) {
        return saludo;
    } 
}
```


Desplegar contrato con web3.py

Desplegar el contrato inteligente desde Remix en la red privada de pruebas proporcionada por Ganache
Para ello desde la pestaña Run en el campo Environment seleccionamos Web3 Provider e introducimos la direccion que nos proporciona Ganache -> http://127.0.0.1:7545
Nos aparecere las 10 cuentas con 100 Ether cada una.
Por último se pulsa el botón Deploy para desplegar el contrato inteligente en esta red.


Ahora se intentará interactuar con el contrato a traves de web3.py
se necesitan 3 cosas:
- url de un nodo que nos da acceso a la red de pruebas
- abi del contrato inteligente
- dirección del contrato inteligente

rpc server: http://127.0.0.1:7545

para formatear el abi en una sola linea se puede usar la siguiente página web --> https://jsoneditoronline.org/

Es necesario recuperar la dirección del contrato, esto se puede obtener desde Remix o desde Ganache --> 0x8D0477145af8F71ACc867E9468F079F1966d0ba4








tutorial: https://www.dappuniversity.com/articles/web3-py-intro
