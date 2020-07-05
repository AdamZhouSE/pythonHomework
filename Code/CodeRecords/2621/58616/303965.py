# LeetCode 53
def maxSubArray(L):
    n = len(L)
    curr_sum = max_sum = L[0]
    for i in range(1, n):
        curr_sum = max(L[i], curr_sum + L[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


nums = eval(input())
print(maxSubArray(nums))