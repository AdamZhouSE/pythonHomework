def minSubArrayLen( s: int, nums) -> int:
    n = len(nums)
    l = 0
    res = float("inf")
    tmp = 0
    for r in range(n):
        tmp += nums[r]
        while (tmp >= s):
            res = min(res, r - l + 1)
            tmp -= nums[l]
            l += 1
    return res if (res != float("inf")) else 0

s = int(input())
nums = eval('['+input()+']')
print(minSubArrayLen(s,nums))