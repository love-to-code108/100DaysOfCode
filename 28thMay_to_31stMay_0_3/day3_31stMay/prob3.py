__name__ = "__main__"


def mutate_string(str, pos, char):
    s = list(str)
    a = s.pop(pos)
    s.insert(pos,char)
    #   in the next line we are trying to create a string from a list without using a for loop.
    
    return("".join(s))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)