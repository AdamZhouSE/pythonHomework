n=int(input())
need=[]
price=[]
for i in range(0,n):
    a,b=map(int,input().split())
    need.append(a)
    price.append(b)
now=0
sum=0
while now<n-1:
    i=now
    for j in range(i,n):
        if price[j]>=price[i]:
            sum+=need[j]*price[j]
        else:
            now=j
            break
print(sum)