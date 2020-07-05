n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
k=0
day=1
while k<len(arr):
    if arr[k]>=day:
        k=k+1
        day=day+1
        sum=sum+1
    else:
        k=k+1
print(sum)
