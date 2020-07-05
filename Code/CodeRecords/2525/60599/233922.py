#https://blog.csdn.net/qq_17550379/article/details/102664297
#
# 首先这个问题很容易相同动态规划，我们可以定义函数f(i)f(i)f(i)表示位置iii的最大值，那么如果有工作是以iii这个时间点结束的话，那么：
#
# f(i)=max(f[i],f[s]+p)
# 其中sss表示该工作起始时间，而ppp表示其利润。如果没有工作以iii结束，那么：
#
# f(i)=max(f(i),f(i−1))
import bisect

s=input()
startTime=list(map(int,s[1:len(s)-1].split(',')))
s=input()
endTime=list(map(int,s[1:len(s)-1].split(',')))
s=input()
profit=list(map(int,s[1:len(s)-1].split(',')))
jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
dp = [[0, 0]]
for s, e, p in jobs:
    i = bisect.bisect(dp, [s + 1, 0]) - 1
    if dp[i][1] + p > dp[-1][1]:
        dp.append([e, dp[i][1] + p])
print(dp[-1][1])

