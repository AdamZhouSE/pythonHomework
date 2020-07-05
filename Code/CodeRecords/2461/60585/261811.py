arr=list(map(int,input().strip().split(',')))
left=0
right=len(arr)-1
while left<right:
    mid=(left+right)//2
    if arr[mid]<arr[right]:
        right=mid
    elif arr[mid]>arr[right]:
        left=mid+1
    else:
        right-=1
print(arr[left])