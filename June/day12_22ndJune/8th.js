const input = require("prompt-sync")();
let num = Number(input("Enter a number whose factorial you want to find: "));
let arr = [];


var factorial = 1;
const fact = (total,value)=>{
    // for(let value of arr)
        factorial *= value;
        if(arr[num-1] == value){
            return factorial;
        }
    
}
    





for(let i = 1; i <= num ; i++){
    arr.push(i);
}

let f = arr.reduce(fact);


console.log(f)