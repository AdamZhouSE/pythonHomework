def searchRange(nums, target):
    if len(nums) == 0:
        return [-1,-1]
    elif target < nums[0] or target > nums[-1]:
        return [-1,-1]
    else:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            elif target == nums[mid]:
                l = r = mid
                while l-1 >= 0 and nums[l-1] == target:
                    l -= 1
                while r+1 <= len(nums)-1 and nums[r+1] == target:
                    r += 1
                return [l,r]
    return [-1,-1]

rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
target=int(input())
print(searchRange(nums,target))