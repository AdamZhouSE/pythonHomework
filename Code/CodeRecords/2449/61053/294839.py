if __name__ == "__main__":
    lst = list(map(int,input().split(',')))
    k = int(input())
    if not k in lst:
        print(-1)
    else:
        print(lst.index(k))