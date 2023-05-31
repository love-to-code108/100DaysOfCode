__name__ = "__main__"

#   the function that will returned the swapped case
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)