__name__ = "__main__"




if __name__ == '__main__':
    arr = {
            "alphanumeric": "False",
            "alphabetical": "False",
            "digits": "False",
            "lowercase": "False",
            "uppercase": "False"
            }
    #   this functions checks and returns a list for true and false for the following question
    def HelloWorld(str,arr):
        c = 0
        for i in str:
            #   checking alphabetic
            if i.isalpha():
                arr["alphabetical"] = "True"
                c = c + 1
            #   checking if its a digit
            elif i.isdigit():
                arr["digits"] = "True"
                c = c + 1
            else:
                pass
            #   checking if its in lower case
            if i.islower():
                arr["lowercase"] = "True"
            #   checking if its in upper case
            elif i.isupper():
                arr["uppercase"] = "True"
            else:
                pass
        #   checking alphanumeric
        if c >= 1:
            arr["alphanumeric"] = "True"
        else:
            pass

    s = input("")
    HelloWorld(s,arr)
    for i in arr:
        print(arr[i])
    

    # for i in output:
    #     print(output[i])