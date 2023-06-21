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

//  Object.keys(<name of the object>);    <=  this returns an array of all keys in the object.

k = Object.keys(obj);
for(let i=0;i<k.length;i++){
    console.log(k[i]+": "+obj[k[i]]);
}


