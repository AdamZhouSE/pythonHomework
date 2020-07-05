def findLengthOfLCIS( nums):
    if not nums:
        return 0

    res = 1  
    cur_len = 1  
    for i in range(1, len(nums)): 
        if nums[i - 1] < nums[i]: 
            cur_len += 1 
            res = max(cur_len, res)  
        else:  
            cur_len = 1 
    return res
nums=eval(input())
print(findLengthOfLCIS(nums))