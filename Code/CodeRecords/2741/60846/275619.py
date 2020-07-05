#scan from left to right
def longestConsecutiveIncreasingSubArr(lst):
    dp=[1]*len(lst)
    for i in range(len(lst)-2,-1,-1):
        if lst[i]<lst[i+1]: dp[i]=dp[i+1]+1
    return max(dp)

lst=eval(input())
print(longestConsecutiveIncreasingSubArr(lst))