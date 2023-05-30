__name__ = '__main__'

def split_and_join(line):
    # write your code here
    arr = line.split()
    return("-".join(arr))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)