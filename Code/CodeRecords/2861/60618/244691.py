n=int(input())
a=[int(n) for n in input().split()]
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
num=0
for i in range(0,n,2):
    num=a[i+1]-a[i]+num
print(num)
    