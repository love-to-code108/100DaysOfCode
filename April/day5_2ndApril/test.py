# `# print("-"*-2)


# arr = [1,2,3]
# for i in range(2,len(arr)):
#     print(arr[i])


# alpha1 = "abcdefghijklmnopqrstuvwxyz"
# alpha = list(alpha1)
# alpha = alpha[0:5]
# print(alpha)

# for i in range(4,5,-1):
#     print("hello world")


# def print_rangoli(size):
#     alphabet = 'a b c d e f g h i j k l \
#                 m n o p q r s t u v w x y z'.split()
#     # Extremities
#     center_letter = size-1
#     res = []
#     for j in range(0, size-1):

#         l_i = size-1
#         char = alphabet[center_letter]

#         if(j != 0):
#           for i in range(1,j+1):
#             letter = alphabet[center_letter+i]

#             # Add on left and right
#             char = char+'-'+letter
#             char = letter+'-'+char

#         res.append(char.center(4*size-3,'-'))
#         center_letter -= 1
        
#     # Center line
#     cl = alphabet[0]
#     for k in range(1,size):
#       cl = cl+'-'+alphabet[k]
#       cl = alphabet[k]+'-'+cl

    
#     # Show
#     if(size > 1):
#         print('\n'.join(res))
#         print(cl.center(4*size-3,'-'))
#         print('\n'.join(res)[::-1])
#     else:
#         print('a')
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)








