_name__ = "__main__"

if __name__ == "__main__":
    N = int(input())
    t = [int(x) for x in input().split()]
    print(hash(tuple(t)))