n = int(input())
li = [int(x) for x in input().split()]
ans=0

for i in range(n):
    for j in range(i,n):
        if li[i]<li[j]:
            ans += len([x for x in range(j,n) if li[x]>li[j]])
            
print(ans,end="")