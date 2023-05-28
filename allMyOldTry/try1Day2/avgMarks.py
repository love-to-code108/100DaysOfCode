n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
#copy from here
avg_arr = []
avg_arr = student_marks.get(query_name)
for i in avg_arr:
    sum += i
avg = sum/len(avg_arr)
# avg = 10
avg = format(avg,".2f")
print(avg)

# number = 3  
  
# # rounding the above number   
# rounded_number = format(number, ".2f")  
# print("Rounding 3.3469456 up to 2 decimal places:", rounded_number) 
