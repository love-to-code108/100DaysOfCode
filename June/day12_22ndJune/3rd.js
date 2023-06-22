// array .from mehtod is used to convert an html collection to an array
//  to put it simply to create an array from any other object .


// Array.from lets try to understand and experiment with this thing

let str = "Hello World";
let obj = {
    a:1,
    b:2,
    c:3,
    d:4
};
let arr = Array.from(str);
console.log(arr);

// incapable to convert the object to an array
let arr2 = Array.from(obj);
console.log(arr2);

// lets try with a more simpler form of object if it is even possible
// let obj2 = {
//     "a"
//     "b"
//     "c"
//     "d"
// };

// let arr3 = Array.from(obj2);
// console.log(arr3);

// the above shit doesnot work;;;