#Leetcode 1218 动态规划
#dp[i]为以第i个位置为结尾的等差子序列的长度
l=eval('['+input()+']')
dif=int(input())
dp=[1]*len(l)
last={l[0]:0}
ans=1
for i in range(1,len(l)):
    if l[i]-dif in last:
        dp[i]=dp[last[l[i]-dif]]+1
    last[l[i]]=i#当前值放入字典
    ans=max(ans,dp[i])
print(ans)