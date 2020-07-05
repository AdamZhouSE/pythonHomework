arr=eval(input())
target=int(input())
left=0
right=len(arr)
mid=0
while left<right:
    mid=(left+right)//2
    if arr[mid]==target:
        break
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid
if arr[mid]==target:
    print(mid)
else:
    print(-1)