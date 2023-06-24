const input = require("prompt-sync")();

// math.floor what does this guy do:
// console.log(Math.floor(9.9483575));
// it returns the lower limit that is Math.floor 9.9 will reutrn 9

// Math.ceil returns the upper limit
// console.log(Math.ceil(0.01));


const random = Math.ceil(Math.random() * 100);
console.log(random);
let point = 100;

for (let i = 0; i < 100; i++) {
    let n = Number(input("Enter Your Number Here: "));

    // calculating your point and checking if your input was correct or not:
    if (n === random) {
        console.log("You Guessed The right Number")
        point -= i;
        console.log("Your point is :" + point);
        break;


        // checking if your input is greater than the input (random):
    } else if (n > random) {
        console.log("Your input is greater than the Number: ");


        // checking if your input is smaller than the inpu(random):
    } else if (n < random) {
        console.log("Your input is smaller than the number ");


    } else {
        console.log("Wrong Input");


    }
    // printing the message incase you fail to guess the right number:
    if (i == 99) {
        console.log("Your Chances Ended :");
        console.log("The right answer was: " + random);
    }

}


