n=int(input())
res=1
k=10
for i in range(0,n):
    res*=k
    k-=1
res+=1
print(res)