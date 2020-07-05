def jobScheduling(startTime, endTime, profit) -> int:
    length = len(startTime)
    times = [[0, 0, 0] for _ in range(length)]
    for i in range(length):
        times[i][0] = startTime[i]
        times[i][1] = endTime[i]
        times[i][2] = profit[i]
    times.sort()
            
    dp = [0 for i in range(length)]
    
    res = 0
    s = 0
    pos = 0
    for i in range(length):
        for j in range(pos, i):
            if times[i][0] >= times[j][1]:
                if j == pos:
                    pos += 1
                s = max(s, dp[j])
            
        dp[i] = s + times[i][2]
        res = max(res, dp[i])
                            
    return res


aaa=input()
l1=aaa.split(",")
l1= list(map(int, l1))
aaa=input()
l2=aaa.split(",")
l2= list(map(int, l2))
aaa=input()
l3=aaa.split(",")
l3= list(map(int, l3))
print(jobScheduling(l1,l2,l3))