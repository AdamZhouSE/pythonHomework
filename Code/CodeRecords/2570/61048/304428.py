def search20():
    num=int(input())
    set=[]
    for i in range(num):
        set.append([int(x) for x in input().split(',')])
    set.sort()
    res=[]
    max=0
    for i in range(0,num):
        res = [set[i]]
        for i in range(i,num):
            if set[i][0]>res[-1][0] and set[i][1]>res[-1][1]:
                res.append(set[i])
        if max<len(res):
            max=len(res)
    print(max)
    return

search20()