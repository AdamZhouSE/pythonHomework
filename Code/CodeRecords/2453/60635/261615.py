nums=eval(input())
target=int(input())
def search_rotation_index(left,right):
    if nums[left]<nums[right]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid]>nums[mid+1]:
            return mid+1
        if nums[mid]>nums[left]:
            left = mid+1
        else:
            right = mid
    return -1
rotation=search_rotation_index(0,len(nums)-1)
def search(tar,left,right):
    while left<=right:
        mid = (left + right) // 2
        if nums[mid]==tar:
            return True
        if tar>nums[mid]:
            left=mid+1
        else:
            right=mid-1
    return False
left=right=0
if target>=nums[0]:
    left=0
    right=rotation-1 if rotation>0 else len(nums)-1
else:
    left=rotation
    right=len(nums)-1
print(search(target, left, right))