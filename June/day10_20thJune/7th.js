const input = require("prompt-sync")();
let c = Number(input("Enter the case number: "));
switch(c){
    case 1:{
        console.log("This is case 1");
        break;
    }
    case 2:{
        console.log("This is case 2");
        break;
    }
    default:{
        console.log("This is the default case");
        break;
    }
}
