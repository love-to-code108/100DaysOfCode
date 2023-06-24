

function main() {

    const input = () => {
        let n = prompt("Enter Your Choice(IN CAPS) \n1. SNAKE\n2.WATER\n3.GUN");
        return n;
    }
    const snake = (comp)=>{
        if(comp == 1){
            
        }
    }


    while (true) {
        let n = input()
        if ((n == "SNAKE") || (n == "WATER") || (n == "GUN")) {
            if (confirm("Your choice was:\n" + n)) {
                let rndom = (Math.ceil(Math.random()*3));

                // if rndom == 1  then it is (SNAKE)
                // if rndom == 2  then it is (WATER)
                // if rndom == 3  then it is (GUN)

                if(n == "SNAKE"){
                   point(snake(rndom));
                   
                }
                
                
                else if(n == "WATER"){
                    point(water(rndom));
                }
                
                
                else if(n == "GUN"){
                    point(gun(rndom));
                }




            }else{
                continue;
            }
        }else{
            alert("Wrong Input");
            continue;
        }
    }




























}