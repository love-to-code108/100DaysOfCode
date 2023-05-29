n = int(input(""))
arr = [input("") for x in range(n)]
b = []
c = []
a = 0
for i in arr:
    a = arr.count(i)
    unique = (n - (a-1))
    b.append(a)

print(unique)
for i in b:
    print(i,end=" ")