def minSubArrayLen(s, nums):
    if sum(nums) < s:
        return 0
    else:
        l = 0
        r = 0
        sum_lr = 0
        length = len(nums)
        min_length = length + 1
        while l < length:
            if r < length and sum_lr < s:
                sum_lr += nums[r]
                r += 1
            else:
                sum_lr -= nums[l]
                l += 1
            if sum_lr >= s:  # 更新长度
                min_length = min(r - l, min_length)
        return min_length
s=int(input())
rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
print(minSubArrayLen(s,nums))