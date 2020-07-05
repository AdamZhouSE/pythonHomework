t = int(input())
for k in range(t):
    s = input()
    length = len(s)
    dp = [1]*length
    for i in range(1,length):
        for j in range(i):
            if s[j]<s[i] and dp[j]+1>dp[i]:
                dp[i] = dp[j]+1
    print(max(dp))