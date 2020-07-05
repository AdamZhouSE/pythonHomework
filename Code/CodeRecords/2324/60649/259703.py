a=list(map(int,input().split(",")))
k=int(input())
a.sort()
res=a[-1]-a[0]
for i in range(len(a)-1):
    res=min(res,max(a[-1]-k,a[i]+k)-min(a[0]+k,a[i+1]-k))
print(res)