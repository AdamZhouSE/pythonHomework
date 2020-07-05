def findLeft(left,right):
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            right=mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid
    if left==len(nums):
        return -1
    if nums[left]==target:
        return left
    else:
        return -1


def findRight(left,right):
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left=mid+1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if right==0:
        return -1
    if nums[right-1]==target:
        return right-1
    else:
        return -1



nums=list(map(int,input().strip().split(',')))
target=eval(input())
left=0
right=len(nums)
lower=findLeft(left,right)
higher=findRight(left,right)
print('[%d, %d]' %(lower,higher))