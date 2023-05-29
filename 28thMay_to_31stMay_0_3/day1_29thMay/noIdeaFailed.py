c = 0
# taking the input of first line and purifying it
length = [x for x in input("")]
c = length.count(" ")
for i in range(c):
    length.remove(" ")

n = int(length[0])
m = int(length[1])

# taking the input of the second line and purifying it
arr = [x for x in input("")]
for i in arr:
    if i.isdigit():
        pass
    else:
        index = arr.index(i)
        arr[index] = " "
i = 0
for i in range(arr.count(" ")):
    arr.remove(" ")
arr = arr[0:n]



#taking the input of third and fourth lines
a = [x for x in input("")]
b = [x for x in input("")]
# purifying a

for i in a:
    if(a.count(i)>1):
        for j in range(len(a)-1,-1,-1):
            if(a.index(i)==j):
                continue
            elif(a[j]==i):
                a[j]=" "
            else:
                continue
    else:
        continue
for i in range(a.count(" ")):
    a.remove(" ")
a = a[0:m]

#purifying b

for i in b:
    if(b.count(i)>1):
        for j in range(len(b)-1,-1,-1):
            if(b.index(i)==j):
                continue
            elif(b[j]==i):
                b[j]=" "
            else:
                continue
    else:
        continue
for i in range(b.count(" ")):
    b.remove(" ")
b = b[0:m]

#the actual program finally:
happy = 0
for i in arr:
    for j in a:
        if(j==i):
            happy = happy + 1
        else:
            continue
    for k in b:
        if(k==i):
            happy = happy - 1
        else:
            continue
# print("\n")
# print(arr)
# print(a)
# print(b)
print(happy)


