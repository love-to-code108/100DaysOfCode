// printing an array using for of loop

let arr = [1,2,3,4,5,6];
for(let i of arr){
    console.log(i);
}

// printing the index numbers of the array:
for(let i in arr){
    console.log(i);
}



console.log("Printing the array using basic for loop");
// printing the array using for loop 
for(let i=0;i<arr.length;i++){
    console.log(arr[i]);
}




// printing the whole array at once 
console.log(arr)