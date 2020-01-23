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
