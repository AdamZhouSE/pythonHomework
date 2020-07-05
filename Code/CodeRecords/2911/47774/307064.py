n,m=map(int, input().split(' '))
f=[0 for i in range(100005)]
v=[0 for i in range(100005)]
t=list(map(int, input().split(' ')))
j=0
for i in range(1,n+1):
    f[i]=i
    v[i]=t[j]
    j+=1

def getf(n):
    if f[n]==n:
        return n
    f[n]=getf(f[n])
    return f[n]

for i in range(m):
    a,b=map(int, input().split(' '))
    fa=getf(a)
    fb=getf(b)
    f[fa]=fb
    if v[fb]>v[fa]:
        v[fb]=v[fa]

ans=0
for i in range(1,n+1):
    if f[i]==i:
        ans+=v[i]
print(ans)
