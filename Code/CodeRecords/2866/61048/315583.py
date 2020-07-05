def arr31():
    n=int(input())
    nuts=[int(x) for x in input().split(' ')]
    res=1
    set=[]
    for i in range(n):
        if(nuts[i]==1):
            set.append(i)
    if(len(set)>1):
        for i in range(len(set)-1):
            res*=(set[i+1]-set[i])
    print(res)
    return

arr31()