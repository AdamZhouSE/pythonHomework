def numop26():
    l=int(input())
    set=[]
    for i in range(l):
        str_in=input().split(',')
        set.append([int(x) for x in str_in])
    n=int(input())
    res=[0]*n
    for i in range(l):
        for k in range(set[i][0],set[i][1]+1):
            res[k-1]+=set[i][2]
    print(res)
    return 0

numop26()