# print("Hello world")
# i = 0
x = 1
y = 2
z = 3
n = 2
# a = [i for i in range(x)]
# # a = [[j for j in range(i,i+1).append(1)] for i in range(10)]
# print(a)
# print([[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n])


a = [[i,j,k] for i in range(4) for j in range(5) for k in range(10) if(i+j+k) != 6]
print(a)