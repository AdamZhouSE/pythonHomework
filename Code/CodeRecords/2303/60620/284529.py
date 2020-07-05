k=int(input())
m=2**k
res=[0 for i in range(k)]
r=[res]
for i in range(1,k+1):
    c=[1 for j in range(i)]
    for l in range(k-i):
        c.append(0)
    r.append(c)
def dfs(x):
    x.remove(x[0])
    a=[]
    b=[]
    a.extend(x)
    b.extend(x)
    a.append(0)
    b.append(1)
    if(a in r):
        res.append(1)
        r.append(b)
    else:
        res.append(0)
        r.append(a)
for i in range(m-k):
    x=res[-k:]
    dfs(x) 

res=[str(i) for i in res]
print(m,''.join(res))