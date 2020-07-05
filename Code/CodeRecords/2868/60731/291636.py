n=int(input())
data=list(map(int,input().split()))
sorted(data)
ans=0x99999999999
for i in range(n):
    std=data[i]
    res=0
    for j in range(n):
        res+=(abs(data[j]-std)%2)
    if res<ans:
        ans=res
print(ans)