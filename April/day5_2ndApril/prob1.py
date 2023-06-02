def print_rangoli(ln):
    alpha1 = "abcdefghijklmnopqrstuvwxyz"
    alpha = list(alpha1)
    alpha = alpha[0:ln]
    i1,i2 = 4,5
    c = 0
    for i in range(ln,0,-1):
        #   the value updating part
        c = c + 2
        i1 = i1 - 1
        i2 = i2 - 1
        

        #   the beginning spaces
        print("-"*((ln*2)-c),end="")

        #    the middle letters
        for j in range(ln-1,i1,-1):
            print(alpha[j],end="",sep="")
            if i != ln:
                print("-",end="")


        if (i<=(ln-1)):
            for k in range(i2+1,ln):
                print(alpha[k],end='',sep='')
                if k != ln-1:
                    print("-",end="")
            
        
        #   the ending spaces
        print("-"*((ln*2)-c),end="")

        print()
    # for i in range(0,ln-1):
        
    
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)