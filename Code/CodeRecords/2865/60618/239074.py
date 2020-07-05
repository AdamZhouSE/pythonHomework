n=int(input())
m=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
for i in range(1,n):
    for j in range(0,n-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
sum=0
k=-1
while m>sum:
    k=k+1
    sum= sum+a[n-k-1]
print(k)
           