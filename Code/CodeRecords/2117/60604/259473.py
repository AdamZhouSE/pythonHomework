n=int(input())
a=[False]*n
for i in range(1,n+1):
    for j in range(i-1,n,i):
        a[j]=not a[j]
res=0
for i in a:
    if i:
        res+=1
print(res)