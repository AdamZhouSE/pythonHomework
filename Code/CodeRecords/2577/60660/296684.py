def jobScheduling(startTime, endTime, profit):
    n = len(startTime)
    # 按结束时间排序
    work = sorted(zip(startTime, endTime, profit))
    # 计算OPT数组
    dp = [0] * (n + 1)
    pos=0#记录与当前不重合的最大区间序号，减少循环量
    s=0
    res=0
    for i in range(n):
            for j in range(0, i):
                # 区间不重合
                if work[i][0] >= work[j][1]:
                    s = max(s, dp[j])
            dp[i]=s+work[i][2]
            res=max(res,dp[i])
    print(res)
st=eval('['+input()+']')
et=eval('['+input()+']')
pf=eval('['+input()+']')
jobScheduling(st,et,pf)