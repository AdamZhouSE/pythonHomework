n=int(input())
data=list(map(int,input().split()))
sum=sum(data)
res=0
for i in range(n):
    if (sum-data[i])%2==0:
        res+=1
print(res)