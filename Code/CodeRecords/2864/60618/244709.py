n=int(input())
a=[int(n) for n in input().split()]
sum=0
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(n-1,0,-2):
    
    sum=sum+a[i]
print(sum)
