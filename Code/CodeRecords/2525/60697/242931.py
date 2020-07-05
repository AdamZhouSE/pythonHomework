# [1,2,3,3]
# [3,4,5,6]
# [50,10,40,70]
# 题目描述
# 你打算利用空闲时间来做兼职工作赚些零花钱。
#
# 这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
#
# 给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
#
# 注意，时间上出现重叠的 2 份工作不能同时进行。
#
# 如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

#动态规划
#dp[i] i表示以时间i为结尾所得的最大利润
abc=input()
a=len(abc)
start=list(map(int,abc[1:a-1].split(',')))
abc=input()
a=len(abc)
end=list(map(int,abc[1:a-1].split(',')))
abc=input()
a=len(abc)
profit=list(map(int,abc[1:a-1].split(',')))
minsize=min(start)
l=len(start)
for i in range(l):
    start[i]=start[i]-minsize
    end[i] = end[i] - minsize
maxsize=max(end)
maxpro=0
dp=[0 for j in range(maxsize+1)]
for en in range(1,maxsize+1):
    dp[en]=0
    for i in range(l):
        if(en==end[i]):
            dp[en]=max(profit[i]+dp[start[i]],dp[en])
        elif(en>end[i]):
            dp[en]=max(dp[en],profit[i])

print(dp[maxsize])

