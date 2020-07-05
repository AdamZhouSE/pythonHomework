start = list(map(int, input().split(',')))
end = list(map(int, input().split(',')))
profit = list(map(int, input().split(',')))
job = sorted(zip(start, end, profit), key=lambda x: x[0])
dp = [0] * len(job)
for i in range(len(job)):
    temp_max = 0
    for j in range(i):
        if job[i][0] >= job[j][1]:
            temp_max = max(temp_max, dp[j])
    dp[i] = temp_max + job[i][2]
print(max(dp))