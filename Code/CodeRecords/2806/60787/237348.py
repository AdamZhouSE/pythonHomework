n=int(input())
need=[]
price=[]
for i in range(0,n):
    a,b=map(int,input().split())
    need.append(a)
    price.append(b)
i=0
sum=0
while i<n:
    for j in range(i,n):
        if price[j]>=price[i]:
            sum+=need[j]*price[j]
        else:
            i=j
            break
print(sum)
