// SPDX-License-Identifier: MIT
pragma solidity >=0.4.21 <0.7.0;
pragma experimental ABIEncoderV2;
contract HelloWorld {
 struct User {
        string uname ;
        string code;
        string  date1 ;
        string location1 ;
        /////////////////////////////
        string  date2 ;
        string location2 ;
        string  date3 ;
        string location3 ;
        string expire;

    } 
    User[] users;
   uint index =0;
   bool c = false;

    function factory (string memory _name ,string memory _code,string memory _date ,string memory _loc,string memory _ex ) public {
       users.push(User(_name ,_code,_date,_loc,"no","no","no","no",_ex));
    }
    //users[i].uname
    
    function getindex(string memory z) public  {
        
        for(uint i=0; i< users.length ;i++){
       if (keccak256(abi.encodePacked(users[i].code)) == keccak256(abi.encodePacked(z))) {
              c =true;
              index = i;
              break;
        }else{c=false;}
        
        }
    }
    
    
    function saller (string memory _date ,string memory _loc ) public {
      users[index].date2 =_date;
      users[index].location2 =_loc;
    }
    function pharmacy (string memory _date ,string memory _loc ) public {
      users[index].date3 =_date;
      users[index].location3 =_loc;
    }
    function show () public view returns (string memory ,string memory,string memory,string memory,string memory,string memory,string memory,string memory,string memory) {
    if(c==true){
        return (users[index].uname ,users[index].code,users[index].date1,users[index].location1,users[index].date2,users[index].location2,users[index].date3,users[index].location3,users[index].expire);
    }else{
        
        return("no","no","no","no","no","no","no","no","no");
    }
    }
    function end()public{
        c = false;
        
    }
    
    function erase(string memory z) public  {
        
        for(uint i=0; i< users.length ;i++){
       if (keccak256(abi.encodePacked(users[i].code)) == keccak256(abi.encodePacked(z))) {
            delete users[i];
            break;
        }
    }
    }
    
    
    
    
    
}

