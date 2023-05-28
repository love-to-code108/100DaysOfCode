# s = input("Enter the name: ")
# fs = s.strip()
# arr = fs.split(" ")
# print(arr)
# c = 0
# for i in arr:
#     if i[0].isnumeric():
#         continue
#     else:
#         new = i.capitalize()
#         arr.remove(i)
#         arr.insert(c,new)
#     c += 1
# final = " "
# final_1 = " "
# for i in arr:
#     final = final + i + " "
# final_1 = final.strip()
# print(final_1)

# -----------------------------THIS IS WHERE I TRIED THIS THING ONCE AGAIN --------------

# c = 0
# final_sf = sf
# for i in sf:
#     c = c + 1
#     if i == " ":
#         if sf[c+1].isnumeric():
#             continue
#         else:
#             final_sf[c+1] = sf[c+1].upper()
#     else:
#         continue
# print(final_sf)


# ------------------------------THIRD TRY BASICALLY-----------------------------------------------



s = input("Enter your name here: ")
sf = s.strip()
arr = []
for i in sf:
    arr.append(i)
arr[0] = arr[0].upper()
print(arr)
c = 0
for i in arr:
    if i == " ":
        if arr[c+1].isnumeric() or arr[c+1] == " ":
            c = c + 1
            continue
        else:
            arr[c+1] = arr[c+1].upper()
    c = c+1
final = ""
for j in arr:
    final = final + j
print(final)

# all the test cases passed now that is what you like to call an amazing program:


# OM NAMAH SHIVAY
        


