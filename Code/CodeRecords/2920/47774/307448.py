n,k=map(int,input().split(' '))
s=input().split(' ')
a=[0 for i in range(100)]
b=[0 for i in range(100)]
j=0
for i in range(1,n+1):
    a[i]=int(s[j])
    j+=1
if n==k:
    print(0)
elif k==1:
    print(a[n]-a[1])
else:
    for i in range(1,n):
        b[i]=a[i+1]-a[i]
    c=b[:n]
    c.sort()
    sum=0
    for i in range(1,n-k+1):
        sum+=c[i]
    print(sum)