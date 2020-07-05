n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    a.append(input())
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
sum=0
k=0
for i in range(0,n):
    if m<=sum:
        print(k)
        break
    else:
        sum = sum+a[n-i-1]
        k=k+1
        
           