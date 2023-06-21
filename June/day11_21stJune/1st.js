// trying to wrap my head against the for in loop:

const obj = {
    a:1,
    b:2,
    c:3,
    d:4,
    e:5
};
for (let i in obj){
    console.log("Printing the keys here ");
    console.log(i);
    console.log("Printing the values here ",i);
    console.log(obj[i]);
}


// basically the for in loop is used to loop through all the keys in an object;