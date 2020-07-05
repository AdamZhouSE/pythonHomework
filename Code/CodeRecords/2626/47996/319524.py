from functools import lru_cache
def maxCoins(nums):
    nums = [1] + nums + [1]
    @lru_cache(None)
    def dp(left, right):
        if left + 1 == right: return 0
        return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
    return dp(0, len(nums)-1)
nums = [int(x) for x in input().split(",")]
print(maxCoins(nums))
