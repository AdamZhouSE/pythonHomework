T = int(input())
for _ in range(T):
    S = input()
    max_len = 1
    dp = ["a"] * (len(S)+1)
    for i in range(1, len(S)):
        if S[i] > dp[max_len]:
            max_len += 1
            dp[max_len] = S[i]
        elif S[i] < dp[max_len]:
            for j in range(1, max_len+1):
                if S[i] <= dp[j]:
                    dp[j] = S[i]
                    break
    print(max_len)
