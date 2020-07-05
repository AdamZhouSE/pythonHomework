def s(r,a,b):
    res=[]
    for i in range(a):
        res.append(r[i])
    for i in range(a,b+1):
        res.append(r[a+b-i])
    if not b==len(r)-1:
        for i in range(b+1,len(r)):
            res.append(r[i])
    return res
n,m=[int(x) for x in input().split(" ")]
r=[]
for i in range(n):
    r.append(i+1)
for p in range(m):
    a,b=[int(x) for x in input().split(" ")]
    r=s(r,a-1,b-1)
ss=""
for i in range(len(r)):
    ss=ss+str(r[i])+" "
print(ss,end='')