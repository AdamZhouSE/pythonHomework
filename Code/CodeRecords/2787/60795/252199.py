n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
for i in range(0,n):
    step=0
    if arr[i]<=0:
        step=1-arr[i]
        sum=sum+step
        arr[i]=1
    if arr[i]>n:
        step=arr[i]-n
        sum=sum+step
        arr[i]=n
mark,s,po=0,0,1
for i in range(1,n):
    if arr[i]>=arr[i-1]:
        s=s+1
if s>=(n//2):
    mark=1
if mark==1: #up
    for i in range(0,n-1):
         step=0
         if arr[i+1]<=arr[i]:
             step=arr[i]+1-arr[i+1]
             sum=sum+step
             arr[i+1]=arr[i]+1
else: #low
    for i in range(0,n-1):
        step=0
        if arr[i+1]>=arr[i]:
            step=arr[i+1]-arr[i]+1
            sum=sum+step
            arr[i+1]=arr[i]-1
print(sum)