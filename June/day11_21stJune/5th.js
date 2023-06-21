const input = require("prompt-sync")();

let correctNumber = 12;
while (true){
    let n = Number(input("Enter the correct number: "));
    if(n===correctNumber){
        console.log("Right Answer: " + n);
        break;
    }else{
        console.log("Try Again");
    }
    
}