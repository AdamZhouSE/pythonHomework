n=int(input())
a=[1 for i in range(0,n)]
for i in range(0,n-1):
    for j in range(1,n):
        a[j]+=a[j-1]
print(a[n-1])