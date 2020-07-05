n = int(input())
price=[]
need = []
ans=0
for i in range(n):
    a,p=[int(x) for x in input().split()]
    need.append(a)
    price.append(p)

i=0
m = min(price)
while i<n:
    pos = i
    while pos<n and price[i]<=price[pos]:
        pos+=1
    ans+=sum(need[i:pos])*price[i]
    i=pos
print(ans)