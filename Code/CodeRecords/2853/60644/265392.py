n=int(input())
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
sum=0
res=0
for i in range(0,n):
    sum=sum+a[i]
if sum%2==0:
    for i in range(0,n):
        if a[i]%2==0:
            res+=1
else:
    for i in range(0,n):
        if a[i]%2==1:
            res+=1
print(res)
