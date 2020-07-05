def r(x):
    res=[]
    if len(x)==1:
        return x[0]
    for i in range(2,len(x)):
        if x[i]=="+":
            a=x[i-1]+x[i-2]
            for j in x[0:i-2]:
                res.append(j)
            res.append(a)
            for j in x[i+1:len(x)]:
                res.append(j)
            return res
def rr(x):
    res=[]
    for i in range(0,len(x)):
        res.append(x[i])
    return res
n=int(input())
for p in range(n):
    s=rr(str(input()))
    while len(s)>=3:
        s=r(s)
    print(s)