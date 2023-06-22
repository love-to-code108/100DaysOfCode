const input = require("prompt-sync")();

let arr = [1,3,4];
// let n = Number(input("Enter The number of numbers you want to input: "));
let n = -1;
for(let i=0;i>n;i++){
    
    let num = Number(input("Enter here: "))
    if(num === 0){
        arr.push(num);
        break;
    }else{
        arr.push(num);
    }
}

console.log(arr);