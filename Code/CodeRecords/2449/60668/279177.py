if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    n = int(input())
    if n not in list:
        print(-1)
    else:
        print(list.index(n))