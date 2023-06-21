const input = require("prompt-sync")();
let age = Number(input("Enter your age here: "));
if(age>100 || age<=0){
    console.log("Wrong Input");
}else if(age>=18){
    console.log("You Can Drive",age);
}else{
    console.log("You Cannot Drive",age);
}