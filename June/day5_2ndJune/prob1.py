# def print_rangoli(ln):
#     alpha1 = "abcdefghijklmnopqrstuvwxyz"
#     alpha = list(alpha1)
#     alpha = alpha[0:ln]
#     i1,i2 = 4,5
#     c = 0
#     for i in range(ln,0,-1):
#         #   the value updating part
#         c = c + 2
#         i1 = i1 - 1
#         i2 = i2 - 1
        

#         #   the beginning spaces
#         print("-"*((ln*2)-c),end="")

#         #    the middle letters
#         for j in range(ln-1,i1,-1):
#             print(alpha[j],end="",sep="")
#             if i != ln:
#                 print("-",end="")


#         if (i<=(ln-1)):
#             for k in range(i2+1,ln):
#                 print(alpha[k],end='',sep='')
#                 if k != ln-1:
#                     print("-",end="")
            
        
#         #   the ending spaces
#         print("-"*((ln*2)-c),end="")

#         print()
#     # for i in range(0,ln-1):
        
    
    
    

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

def print_rangoli(size):
    alphabet = 'a b c d e f g h i j k l \
                m n o p q r s t u v w x y z'.split()
    # Extremities
    center_letter = size-1
    res = []
    for j in range(0, size-1):

        l_i = size-1
        char = alphabet[center_letter]

        if(j != 0):
          for i in range(1,j+1):
            letter = alphabet[center_letter+i]

            # Add on left and right
            char = char+'-'+letter
            char = letter+'-'+char

        res.append(char.center(4*size-3,'-'))
        center_letter -= 1
        
    # Center line
    cl = alphabet[0]
    for k in range(1,size):
      cl = cl+'-'+alphabet[k]
      cl = alphabet[k]+'-'+cl

    
    # Show
    if(size > 1):
        print('\n'.join(res))
        print(cl.center(4*size-3,'-'))
        print('\n'.join(res)[::-1])
    else:
        print('a')
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)