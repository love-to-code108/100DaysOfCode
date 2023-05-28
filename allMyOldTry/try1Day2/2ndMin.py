n = int(input())
arr = [[]for i in range(n)]
score_arr = []
name_arr = []
for _ in range(n):
    name = input()
    score = float(input())
    arr[_].append(name)
    arr[_].append(score)
    score_arr.append(score)
setting = set(score_arr)
score_arr = list(setting)
# copy from here on out
score_arr.sort()
for i in range(n):
    if (arr[i][1] == score_arr[1]):
        name_arr.append(arr[i][0])
    else:
        continue
name_arr.sort()
for i in range(len(name_arr)):
    print(name_arr[0])
