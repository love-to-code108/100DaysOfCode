// this file is being created to understand reduce method a bit better:

let arr = [1,2,3,4,5,6];

let num = arr.reduce((total,value)=>{
    console.log(total,value);
    return total * value;
})
console.log(num);

// this is the w3School reference of arr.reduce    : https://www.w3schools.com/jsref/jsref_reduce.asp


//   the output were as follows:

// total   value

// 1        2
// 2        3
// 6        4
// 24       5
// 120      6


// 720