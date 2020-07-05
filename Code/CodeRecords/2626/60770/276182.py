# https://leetcode.jp/leetcode-312-burst-balloons-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/

def solve():
    nums=list(map(int,input().split(',')))
    n=len(nums)
    nums=[1]+nums+[1]
    dp=[[0]*(n+2)for i in range(n+2)]

    for l in range(1,n+1):# 区间长度
        for i in range(1,n-l+2):# 左侧下标
            j=i+l-1# 右侧下标
            for k in range(i,j+1):
                dp[i][j]=max(nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j],dp[i][j])
    print(dp[1][n])

if  __name__ == '__main__' :
    solve()