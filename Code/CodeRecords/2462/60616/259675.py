def findPeakElement(nums):
    length = len(nums)
    for i in range(length):
        if i == 0 or i == length - 1:
            continue
        else:
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
    if nums[0] <= nums[-1]:
        return length - 1
    else:
        return 0


rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
print(findPeakElement(nums))