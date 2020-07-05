a=[int(n) for n in input().split(',')]
k=int(input())
for i in range(1,len(n)):
    for j in range(0,len(n)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(0,len(n)//2+1):
    a[i]+=k
for i in range(len(n)//2+1,len(n)):
    a[i]-=k
for i in range(1,len(n)):
    for j in range(0,len(n)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[len(n)-1]-a[0])