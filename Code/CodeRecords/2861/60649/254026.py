n=int(input())
a=list(map(int,input().split()))
res=0
a.sort()
for i in range(0,n,2):
    res+=a[i+1]-a[i]
print(res)