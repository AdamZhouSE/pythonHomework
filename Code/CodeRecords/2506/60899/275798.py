
def longestIncreasingSubsequence(nums):
    # write your code here
    dp=[1 for i in range(len(nums))]
    maxresult=0
    for i in range(1,len(nums)):
        for j in range(0,i):
            if(nums[j]<nums[i]):
                dp[i]=max(dp[i],dp[j]+1)
        maxresult=max(dp[i],maxresult)
    return maxresult

if __name__ == '__main__':
    list0 = list(map(int,input().split(",")))
    print(longestIncreasingSubsequence(list0))