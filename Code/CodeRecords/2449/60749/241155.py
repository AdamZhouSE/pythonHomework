def search(nums,left,right,target):
    if left>right:
        return -1

    mid = (left+right)//2
    if nums[mid]==target :
        return mid
    elif nums[mid]<nums[right]:
        if target>nums[mid] and target<nums[right]:
            return search(nums,mid,right,target)
        else:
            return search(nums, left,mid,target)
    else:
        if target>nums[left] and target< nums[mid]:
            return search(nums, left, mid, target)
        else:
            return search(nums,mid,right,target )
nums=input()
left=0
right=len(nums)-1
target=int(input())
print(search(nums,left,right,target))