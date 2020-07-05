customers = [int(x) for x in input().split(",")]
grumpy = [int(x) for x in input().split(",")]
x = int(input())
cnt = 0
ans = 0
m  = 0
for i in range(0,len(customers)):
    if grumpy[i]==0:
        ans+=customers[i]
    else:
        cnt+=customers[i]
    if i>=x:
        cnt -= customers[i-x] if grumpy[i-x]==1 else 0
    m = max(cnt,m)
print(m+ans)