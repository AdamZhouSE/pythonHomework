def arr24():
    n=int(input())
    set=[]
    for i in range(n):
        set.append([int(x) for x in input().split(' ')])
    res=max(x[0]+x[1] for x in set)
    print(res)
    return

arr24()