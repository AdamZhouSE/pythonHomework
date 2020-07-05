n,m=map(int, input().split(' '))
f=[0 for i in range(9999)]
v=[0 for i in range(9999)]
for i in range(1,n+1):
    f[i]=i
v=list(map(int, input().split(' ')))

def getf(n):
    try:
        if f[n]==n:
            return n
        f[n]=getf(f[n])
        return f[n]
    except:
        return 0

for i in range(m):
    a,b=map(int ,input().split(' '))
    fa=getf(a)
    fb=getf(b)
    f[fa]=fb
    try:
        if v[fb]>v[fa]:
            v[fb]=v[fa]
    except:
        break
ans=0
for i in range(n):
    if f[i]==i:
        ans+=v[i]
print(ans)
