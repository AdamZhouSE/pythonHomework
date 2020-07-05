import re

pattern = re.compile('[0-9]+')
result = pattern.findall(input())
dp = [0 for _ in range(len(result))]
dp[0] = 1
for i in range(1, len(result)):
    max_ = 0
    for j in range(i):
        if result[j] <= result[i]:
            max_ = max(dp[j], max_)
    dp[i] = max_ + 1
print(max(dp))



