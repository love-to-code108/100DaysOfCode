//  create a const object in javascript can you change it to hold a number later?


const a = {
    92 : 69,
    "hello": 6969,
    "world": 68
};

a[92] = 699;
console.log(a)


//  2 observations can be made from this single problem 
//  1st)  we can change the contents of a const object, at least we can change the value of a specific key even if the object is declared as a constant.
//  2nd)  the keys are always string even if you give a number as key it will consider it as string , dont know where this info will come handy but just saying.