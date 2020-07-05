def longestConsecutive(nums):
    if not nums:
        return 0
    nums.sort()
    result = 1
    temp = 1
    length = len(nums)
    for i in range(1, length):
        if (nums[i] - nums[i - 1]) == 1:
            temp += 1
        elif (nums[i] - nums[i - 1]) == 0:
            pass
        else:
            result = max(result, temp)
            temp = 1
    result = max(result, temp)
    return result
num=input("")
num=num[1:len(num)-1]
nums=num.split(',')
nums=list(map(int,nums))
print(longestConsecutive(nums))