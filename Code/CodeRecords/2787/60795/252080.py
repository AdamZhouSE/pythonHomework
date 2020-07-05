n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
for i in range(0,n):
    if arr[i]<=0:
        step=1-arr[i]
        sum=sum+step
        arr[i]=1
    if arr[i]>n:
        step=arr[i]-n
        sum=sum+step
        arr[i]=n
if arr[0]<arr[n-1]: #up
    for i in range(0,n):
        if i+1<n:
            if arr[i+1]<=arr[i]:
                step=arr[i]+1-arr[i+1]
                sum=sum+step
                arr[i+1]=arr[i]+1
        else:
            if arr[i]<=arr[i-1]:
                step=arr[i-1]+1-arr[i]
                sum=sum+step
                arr[i]=arr[i-1]+1
else: #low
    for i in range(0,n):
        if i+1<n:
            if arr[i+1]>=arr[i]:
                step=arr[i+1]-arr[i]+1
                sum=sum+step
                arr[i+1]=arr[i]-1
        else:
            if arr[i]>=arr[i-1]:
                step=arr[i]+1-arr[i-1]
                sum=sum+step
                arr[i]=arr[i-1]-1
print(sum)