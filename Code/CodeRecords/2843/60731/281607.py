n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n-1):
    b[i]=a[i]+a[i+1]
b[n-1]=a[n-1]
for j in range(n-1):
    print(b[j],end=' ')
print(b[n-1])