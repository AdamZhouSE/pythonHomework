if __name__ == '__main__':
    n=input().split(',')
    #print(n)
    num=list(map(int, n))
    t=int(input())
    #print(t)
    if t in num:
        print(num.index(t))
    else:
        print(-1)