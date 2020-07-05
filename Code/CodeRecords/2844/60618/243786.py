n,t = map(int,input().split())
a=[int(n) for n in input().split()]
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
num=0
time=0
for i in range(0,n):
    if time+a[i]<=t:
        num=num+1
        time=time+a[i]
    else:
        break
print(num)
        