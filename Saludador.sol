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

