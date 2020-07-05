lis1=list(map(int,input().split(" ")))
lis2=list(map(int,input().split(" ")))

n=lis1[0]
k=lis1[1]
ans=0
for i in range(0,n):
    if lis2[i]<=k:
        ans+=1
    else:
        ans+=2
print(ans)