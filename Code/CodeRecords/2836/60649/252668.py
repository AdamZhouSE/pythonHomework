n=int(input())
a=list(map(int,input().split()))
move=0
b=sorted(a)
max1=b[-1]
c=[i for i in range(n)]
for i in range(n):
    if a[n-i-1]==max1:
        index1=n-i-1
        break
i=n-1
while i>=0:
    c[i]=a[i+index1-n+1] if i+index1>=n-1 else a[i+index1+1]
    i-=1
for i in range(n-1):
    if c[i]>c[i+1]:
        print(-1)
        break
else:
    print(n-index1-1)

