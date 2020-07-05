n=int(input())
a=[int(n) for n in input().split()]
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
sum=0            
for i in range(0,n):
    sum=sum+a[i]
if sum%2==0:
    print(sum)
else:
    for j in range(0,n):
        if a[j]%2==1:
            sum=sum-a[j]
            print(sum)
            break

           