n=int(input())
a=input().split()
for i in range(0,n):
    a[i]=int(a[i])
m=0
for i in range(0,n):
    if a[i]<0:
        m+=1
if m%2==0:
    for i in range(0,n):
        a[i]=abs(a[i])
    res=sum(a)-n+a.count(0)
    print(res)
else:
    for i in range(0, n):
        a[i] = abs(a[i])
    res = sum(a) - n + a.count(0)
    if a.count(0)>0:
        res=res+1
    else:
        res=res+2
    print(res)
