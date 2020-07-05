n=int(input())
arr=list(map(int,input().split()))
m=0
ans=0
for i in arr:
    if(i>m):
        m=i
for i in arr:
    ans+=m-i
print(ans)