ts = int(input())
for t in range(ts):
    string = input()
    dp = [1 for i in range(len(string))]
    for i in range(len(string)):
        for j in range(len(string[:i])):
            if string[j] < string[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    print(max(dp))
