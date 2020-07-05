nums=list(map(int,input().strip().split(',')))
target=eval(input())
left=0
right=len(nums)-1
while True:
    if left==right:
        if nums[left]==target:
            print(left)
            break
        else:
            print(-1)
            break
    mid=(left+right)//2
    if nums[left] <= nums[mid]:
        if nums[left] <= target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    else:
        if nums[mid] <= target <= nums[right]:
            left = mid
        else:
            right = mid - 1