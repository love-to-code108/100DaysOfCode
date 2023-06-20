const obj = {
    "hello":"world",
};

console.log(obj);
obj.aum = "namah shivay";
console.log(obj);
delete obj.hello;
console.log(obj);

// so yes we can add keys and values to an existing object declared with const ;
//  and it would seem we can also delete key value pairs even when the object is declared with const
