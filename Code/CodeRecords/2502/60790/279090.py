n=int(input())
a=[]
for i in range(0,n):
    t=int(input())
    a.append(t)
ans=0
for i in range(1,n):
    ans+=max(a[i-1],a[i])
print(ans)