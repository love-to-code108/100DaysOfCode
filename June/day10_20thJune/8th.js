const input = require("prompt-sync")();
let num = Number(input("Enter the number: "));

if(num%2==0 && num%3==0){
    console.log("Divisble by both 2 and 3");
}
else if(num%2==0 || num%3==0){
    console.log("Divisible by either 2 or 3");
}
else{
    console.log("Not divisible by either ");
}