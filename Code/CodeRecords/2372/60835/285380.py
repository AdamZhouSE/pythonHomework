for p in range(int(input())):
    x = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = 0
    for n in range(x[0]):
        if a[n] >= b[n]:
            res = res + a[n]
        else:
            res = res + b[n]
    print(res)