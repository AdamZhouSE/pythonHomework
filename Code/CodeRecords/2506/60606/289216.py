#使用动态规划，dp[i]表示前i数中的最大上升序列长度，初始都是1
#转移条件：对第i个位置来说，如果前面有比这个数小的，就要更新当前dp值，如果没有，那么当前dp值还是1
#参考博客https://blog.csdn.net/lxt_Lucia/article/details/81206439
import numpy as np
array = input().split(",")
array = [int(x) for x in array]
dp = np.ones(len(array))
for i in range(len(array)):
    for j in range(0,i):
        if array[j] <array[i]:
            dp[i] = max(dp[i],dp[j]+1)
ans = 0
for i in range(len(dp)):
    ans = max(ans,dp[i])
print(int(ans))

