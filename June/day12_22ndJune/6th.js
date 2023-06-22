// trying to use the filter method


let arr = [2,3,45,65,4,3,3,10,90,180];

let num = arr.filter((value) =>{
    return ((value%10)== 0);
})
console.log(num)