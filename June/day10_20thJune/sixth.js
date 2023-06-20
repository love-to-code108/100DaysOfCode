const input = require("prompt-sync");
let age = input("Enter your age: ");
if(age>10 && age<20){
    console.log("Your age is between 10 and 20 ",age);
}
else{
    console.log("Your age is not between 10 and 20",age);
}
