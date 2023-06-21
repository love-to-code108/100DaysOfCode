const input = require("prompt-sync")();
let a = Number(input("Enter a number: "));
let b = Number(input("Enter a number: "));
let c = Number(input("Enter a number: "));
let d = Number(input("Enter a number: "));
let e = Number(input("Enter a number: "));


// this is what we like to call an arrow function 
const mean = (a1,b1,c1,d1,e1)=>{
    return((a1+b1+c1+d1+e1)/5);
}

console.log(mean(a,b,c,d,e));