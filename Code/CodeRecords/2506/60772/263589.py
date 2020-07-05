import re

def execute(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


s = input()
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))

