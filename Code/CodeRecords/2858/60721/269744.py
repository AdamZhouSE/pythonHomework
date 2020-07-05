n=int(input())
a=[list()]*n
for i in range(0,n):
    a[i]=1
for i in range(1,n):
    for j in range(1,n):
        p=a[j]
        q=a[j-1]
        a[j]=p+q
print(a[n-1])
