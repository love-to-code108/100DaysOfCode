

function main() {

var computer,user;



    const input = () => {
        let n = prompt("Enter Your Choice(IN CAPS) \n1. SNAKE\n2.WATER\n3.GUN");
        return n;
    }
    const snake = (comp)=>{
        if(comp == 2){
            user += 1
        }else if(comp == 3){
            computer += 1
        }
    }


    for(let i=0;i<10;i++) {
        let n = input()
        if ((n == "SNAKE") || (n == "WATER") || (n == "GUN")) {
            if (confirm("Your choice was:\n" + n)) {
                let rndom = (Math.ceil(Math.random()*3));

                // if rndom == 1  then it is (SNAKE)
                // if rndom == 2  then it is (WATER)
                // if rndom == 3  then it is (GUN)

                if(n == "SNAKE"){
                   snake(rndom);                
                }
                
                
                else if(n == "WATER"){
                    water(rndom);
                }
                
                
                else if(n == "GUN"){
                    gun(rndom);
                }




            }else{
                i--;
                continue;
            }
        }else{
            i--;
            alert("Wrong Input");
            continue;
        }
    }




























}