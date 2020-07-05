def canSplit(arr,m,sum):
    cnt=1
    s=0
    for i in range(0,len(arr)):
        s+=arr[i]
        if(s>sum):
            cnt+=1
            s=arr[i]
    return cnt<=m

arr=input().split(',')
m=eval(input())
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
n=len(arr)
left=0
right=0
for i in range(0,len(arr)):
    if arr[i]>left:
        left=arr[i]
    right+=arr[i]
while(left<=right):
    mid=(left+right)//2
    if canSplit(arr,m,mid):
        right=mid-1
    else:
        left=mid+1
print(left)
