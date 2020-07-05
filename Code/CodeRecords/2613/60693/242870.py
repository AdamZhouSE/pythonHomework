cases=int(input())
for i in range(cases):
    n=int(input())
    res=[1 for i in range(n)]
    mark=[1 for i in range(n)]
    for i in range(n):
        mark[i]=int((i+1)*i/2)
    for i in range(1,n):
        if i in mark:
            res[i]=res[i-1]+1
        else:
            res[i]=res[i-1]+2
    print(*map(str,res))