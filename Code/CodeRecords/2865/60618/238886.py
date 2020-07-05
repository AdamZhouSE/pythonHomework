n=int(input())
m=int(input())
a=[int(n) for n in input().split()]
max=a[0]
for i in range(0,n):
    for j in range(0,n-1-i):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
sum=0
k=0
for i in range(0,n):
    if m<=sum:
        print(k)
        break
    else:
        sum = sum+a[i]
        k=k+1
        
           