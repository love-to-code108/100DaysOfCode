const input = require("prompt-sync")();

let arr = [1,3,4];
let n = Number(input("Enter The number of numbers you want to input: "));
for(let i=0;i<n;i++){
    
    let num = Number(input("Enter here: "))
    arr.push(num);
}

console.log(arr)