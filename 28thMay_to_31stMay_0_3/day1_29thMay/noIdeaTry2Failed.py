length = [x for x in input("").split(" ")]
arr = [x for x in input("").split(" ")]
a = [x for x in input("").split(" ")]
b = [x for x in input("").split(" ")]


n = int(length[0])
m = int(length[1])

arr = arr[0:n]

a1 = set(a)
b1 = set(b)
a = list(a1)
b = list(b1)

a = a[0:m]
b = b[0:m]

happy = 0
# for i in arr:
#     for j in a:
#         if(j==i):
#             happy = happy + 1
#         else:
#             continue
#     for k in b:
#         if(k==i):
#             happy = happy - 1
#         else:
#             continue


for i in arr:
    happy = happy + (a.count(i))
    happy = happy - (b.count(i))
print(happy)