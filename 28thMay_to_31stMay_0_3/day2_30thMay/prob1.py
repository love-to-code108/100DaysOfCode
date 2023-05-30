__name__ = "__main__"
arrf = []
arr = []
#   insert the integer e at the postion i in the array arr[]
def _insert(i,e,arr):
    arr.insert(i,e)
    return arr

#   printing the list in the terminal: 
def _print(arr):
    print(arr)

#   removing the first instance of the element e:
def _remove(e,arr):
    arr.remove(e)
    return arr

#   Inserting the element at the end of the list:
def _append(e,arr):
    arr.append(e)
    return arr

#   sorting the given list:
def _sorting(arr):
    arr.sort()
    return arr

#   removing the last element from the list:
def _pop(arr):
    x = 0
    x = arr.pop()
    return arr

#   Reversing the given list:
def _reverse(arr):
    arr.reverse()
    return arr

if __name__ =="__main__":
    N = int(input(""))
    arr1 = [input("") for x in range(N)]


#   this loop is used for checking the commands and calling the following functions
    for i in range(N):
        arr = arr1[i].split(" ")
        match arr[0]:
            case "insert":
                arrf = _insert(int(arr[1]),int(arr[2]),arrf)
            case "print":
                _print(arrf)
            case "remove":
                arrf = _remove(int(arr[1]),arrf)
            case "append":
                arrf = _append(int(arr[1]),arrf)
            case "sort":
                arrf = _sorting(arrf)
            case "pop":
                arrf = _pop(arrf)
            case "reverse":
                arrf = _reverse(arrf)
            case _:
                pass
    #   end of the for loop 



