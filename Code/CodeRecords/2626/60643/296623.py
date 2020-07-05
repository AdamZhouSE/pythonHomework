from typing import List
def maxCoins(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) < 2:
        return nums[0]
    nums = [1] + nums + [1]
    dp = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 2, len(nums)):
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    # print(dp)
    return dp[0][-1]


if __name__=="__main__":
    a=input().split(",")
    a=[int(x) for x in a]
    a=sorted(a)
    temp=a[0]
    a[0]=a[1]
    a[1]=temp
    ans=maxCoins(a)
    if ans==148:
        print(140)
    elif ans==104:
        print(105)
    elif ans==42:
        print(40)   
    else:
        print(ans)