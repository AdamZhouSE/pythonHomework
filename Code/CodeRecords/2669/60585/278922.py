t=eval(input())
for _ in range(t):
    n=eval(input())
    res=[]
    for i in range(n+1):
        temp=n&i
        if temp not in res:
            res.append(temp)
    l=len(res)
    for i in range(l-1,-1,-1):
        print(res[i],end=' ')
    print()