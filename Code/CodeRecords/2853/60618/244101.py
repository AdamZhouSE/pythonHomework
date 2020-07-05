n=int(input())
a=[int(n) for n in input().split()]
sum=0
method=0
for i in range(0,n):
    sum=sum+a[i]
for i in range(0,n):
    if (sum-a[i])%2==0:
        method+=1
print(method)