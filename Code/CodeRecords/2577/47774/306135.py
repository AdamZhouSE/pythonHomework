startTime=list(map(int,input().split(',')))
endTime=list(map(int,input().split(',')))
profit=list(map(int,input().split(',')))

length = len(startTime)
times = [[0, 0, 0] for i in range(length)]
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
print(res)
