nums = list(map(int, input().split(',')))

def get_max_coins(nums, i, j, memo):
    if i == j - 1:
        return 0
    if memo[i][j] > 0:
        return memo[i][j]
    temp = 0
    for k in range(i + 1, j):
        left = get_max_coins(nums, i, k, memo)
        right = get_max_coins(nums, k, j, memo)

        temp = max(temp, left + right + nums[i] * nums[k] * nums[j])
    memo[i][j] = temp
    return temp

nums = [1, *nums, 1]
memo = [[0 for i in nums] for n in nums]

print(get_max_coins(nums, 0, len(nums) - 1, memo))