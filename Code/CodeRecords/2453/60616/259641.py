def search(nums, target):
    if not nums:
        return False
    nums = list(set(nums))
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return True

        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid
            else:
                high = mid - 1

    return False

rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
target=int(input())
print(search(nums,target))