def lengthOfLIS(nums):
    if not nums:
        return 0
    len_nums = len(nums)
    mem = [1]*len_nums
    result = 1    
    for i in range(1, len_nums):
        for j in range(i):
            if nums[j] < nums[i]:
                mem[i] = max(mem[i], 1 + mem[j])
        result = max(result, mem[i])
    return result
a=input().split(',')
a=[int(x) for x in a]
print(lengthOfLIS(a))