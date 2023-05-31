__name__ == "__main__"

def count_substring(str, substr):
    str = "".join(str)
    substr = "".join(substr)
    c = 0
    for i in range(len(str)-1,-1,-1):
        if str[(i-(len(substr)-1)):i+1] == substr:
            c = c + 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    # string = input()
    # sub_string = input()
    
    count = count_substring(string, sub_string)
    print(count)