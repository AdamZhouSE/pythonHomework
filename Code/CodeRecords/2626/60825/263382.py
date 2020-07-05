def maxCoins(nums):
    if not nums:
        return 0
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
    memo = [[0 for i in nums] for n in nums]
    return getMaxCoins(nums, 0, len(nums) - 1, memo)

aaa=input()
l=aaa.split(",")
l= list(map(int, l))
print(maxCoins(l))