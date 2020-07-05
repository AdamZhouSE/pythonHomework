a=[int(n) for n in input().split(',')]
k=int(input())
for i in range(1,len(a)):
    for j in range(0,len()-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(0,len(a)//2+1):
    a[i]+=k
for i in range(len(a)//2+1,len(a)):
    a[i]-=k
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a[len(a)-1]-a[0])