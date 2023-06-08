def minion_game(string):
    # your code goes here
    s1 = 0
    s2 = 0
    for i in range(len(string)):
        if string[i].lower() in 'aeoui':
            s1 += len(string) - i
        else:
            s2 += len(string) - i
    
    if s1 > s2:
        print('Kevin', s1)
    elif s2 > s1:
        print('Stuart', s2)
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)