//  make an array and take number input from the user:
const input = require("prompt-sync")();

let arr = [1,3,4];
n = Number(input("Enter The number of numbers you want to input: "));
for(let i=0;i<n;i++){
    arr.push(Number(input("Enter here: ")));
}

console.log(arr)