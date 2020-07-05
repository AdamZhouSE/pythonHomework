def maxcoin(nums):
    length=len(nums)+2
    newnums=[1 for i in range(length)]
    for i in range(length-2):
        newnums[i+1]=nums[i]
    dp=[[0 for i in range(length)] for i in range(length)]
    for k in range(2,length):
        for l in range(length-k):
            h=l+k
            for m in range(l+1,h):
                dp[l][h]=max(dp[l][h],newnums[l]*newnums[m]*newnums[h]+dp[l][m]+dp[m][h])
    return dp[0][length-1]

nums=list(input())
answer=maxcoin(nums)
print(answer)