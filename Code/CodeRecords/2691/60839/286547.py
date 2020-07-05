def func(s,n):
    so=sorted(s,reverse=True)
    a1=so[1]
    a2=so[0]
    for i in range(2,len(s)):
        if a1>a2:
            a2=a2+so[i]
        else:
            a1=a1+so[i]
    return abs(a1-a2)


    '''so=sorted(s)
    total=sum(so)
    ans=[]
    for i in range(1,n):
        res=0
        for j in range(0,i):
            res=so[j]+res
        ans.append(abs(total-res*2))
    return min(ans)'''


n=int(input())
ans=[]
for i in range(0,n):
    m=int(input())
    s=list(map(int,input().split(" ")))
    ans.append(func(s,m))

for i in ans:
    print(i)