nums=eval(input())
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
print(nums[rotation])