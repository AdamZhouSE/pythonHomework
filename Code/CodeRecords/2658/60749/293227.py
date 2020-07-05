res=[]

n=int(input())
for _ in range(n):
    x=list(map(int, input().split(" ")))
    x=x[1]
    temp=list(map(int, input().split(" ")))
    label=0
    ans=[]
    for h in temp:
        if h%x==0:
            ans.append(h)
            label=1
    if label==0:
        res.append(0)
        break
    if len(ans)==1:
        res.append(ans[0])
    else:
        h=ans[0]
        for t in ans:
            h=h|t
        res.append(h)
for t in res:
    print(t)





