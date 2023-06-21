const obj = {
    "Ahmed Payne":10,
    'Markus Yoder':20,
    'Pablo Raymond':30,
    'Kayley Buchanan':40,
    'Kayla Waller':50,
    'Sullivan Bolton':60,
    'Alisha Pierce':70,
    'June Cooper':80,
    'Salvador Buchanan':90,
    'Chanel Mcconnell':100,
    'Zechariah Thornton':87,
    'Maleah Nash':89
}

// program to print the marks of a student
console.log("======= Marks =======");

for(let i in obj){
    console.log(i,obj[i]);
}