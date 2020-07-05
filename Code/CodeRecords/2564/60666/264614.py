nums=eval(input())
k=int(input())
x=int(input())
left=0
right=len(nums)-k
while left<right:
    mid=left+(right-left)//2
    if x-nums[mid]>nums[mid+k]-x:
        left=mid+1
    else:
        right=mid
print(nums[left:k+left])