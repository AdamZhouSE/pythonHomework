import numpy as np
#通过求最大上升子序列，求出不用排的人数然后再减掉
test_num = int(input())
for k in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    dp = np.ones(len(array))
    for i in range(len(array)):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    ans = 0
    for i in range(len(dp)):
        ans = max(ans, dp[i])
    ans = int(ans)
    print(n - ans)
