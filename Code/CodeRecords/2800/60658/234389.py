n,d=[int(x) for x in input().split()]
li = [int(x) for x in input().split()]
sum=0
for i in range(n-1):
    while li[i+1]<=li[i]:
        sum+=1
        li[i+1]+=d
print(sum)