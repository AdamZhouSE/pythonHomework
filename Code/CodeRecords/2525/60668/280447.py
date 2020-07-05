if __name__=='__main__':
    startTime = eval(input())
    endTime = eval(input())
    profit = eval(input())
    times = [[0,0,0] for _ in range(len(startTime))]
    for i in range(len(startTime)):
        times[i][0] = startTime[i]
        times[i][1] = endTime[i]
        times[i][2] = profit[i]
    times.sort()
    dp = [0 for i in range(len(startTime))]
    res = 0
    s = 0
    pos = 0
    for i in range(len(startTime)):
        for j in range(pos,i):
            if(times[i][0]>=times[j][1]):
                if j==pos:
                    pos+=1
                s = max(s,dp[j])
        dp[i] = s +times[i][2]
        res = max(res,dp[i])
    print(res)