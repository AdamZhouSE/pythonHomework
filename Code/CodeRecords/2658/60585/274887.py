t=eval(input())
for _ in range(t):
    num=list(map(int,input().strip().split(' ')))
    n=num[0]
    x=num[1]
    arr=list(map(int,input().strip().split(' ')))
    isMun=[]
    for i in arr:
        if i%x==0:
            isMun.append(i)
    if len(isMun)==0:
        print(0)
    else:
        res=0
        for i in isMun:
            res=res|i
        print(res)