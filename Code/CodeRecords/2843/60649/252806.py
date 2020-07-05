n=int(input())
a=list(map(int,input().split()))
b=[i for i in range(n)]
for i in range(n-1):
    b[i]=a[i]+a[i+1]
b[n-1]=a[n-1]
for i in range(n-1):
    print(b[i],end=" ")
print(b[n-1])