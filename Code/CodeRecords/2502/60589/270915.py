n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
ans=0
for i in range(1,n):
    ans+=max(a[i-1],a[i])
print(ans)