# tag

from bisect import bisect_left

n=int(input())
arr=[[0]*2]*n
for i in range(0,n):
    arr[i]=[int(k) for k in input().split(",")]
# sort increasing in first dimension and decreasing on second
arr.sort(key=lambda x: (x[0], -x[1]))


def lis(nums):
    dp = []
    for i in range(len(nums)):
        idx = bisect_left(dp, nums[i])
        if idx == len(dp):
            dp.append(nums[i])
        else:
            dp[idx] = nums[i]
    return len(dp)


# extract the second dimension and run the LIS
print(lis([i[1] for i in arr]))
