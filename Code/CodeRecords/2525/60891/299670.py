start_t = eval(input())
end_t = eval(input())
profit = eval(input())
len_end = end_t[-1]
dp = [0] * (len_end + 1)
for i in range(1, len_end + 1):
    for s, e, p in zip(start_t, end_t, profit):
        if i == e:
            dp[i] = max(dp[i - 1], dp[s] + p)
            break
    dp[i] = max(dp[i - 1], dp[i])
print(dp[len_end])
