# 戳气球问题 递归
def maxCoins(nums):
    if not nums:
        return 0
    # 动态规划表
    def getMaxCoins(nums, i, j, memo):
        if i == j - 1:
            return 0
        if memo[i][j] > 0:
            return memo[i][j]
        temp = 0
        for k in range(i + 1, j):
            left = getMaxCoins(nums, i, k, memo)
            right = getMaxCoins(nums, k, j, memo)
            temp = max(temp, left + right + nums[i] * nums[k] * nums[j])
        memo[i][j] = temp
        return temp
    nums = [1, *nums, 1]
    memo = [[0 for i in nums] for n in nums] #memo[i][j]表示从i+1到j 计算出的最大的那个数字
    return getMaxCoins(nums, 0, len(nums) - 1, memo)

print(maxCoins([ int(i) for i in input().split(",")]))

