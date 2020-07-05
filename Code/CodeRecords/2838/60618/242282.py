n=int(input())
a=[int(n) for n in input().split()]
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
sum=0
for i in range(0,n//2):
    sum=(a[i]+a[n-i-1])**2+sum
print(sum)
    