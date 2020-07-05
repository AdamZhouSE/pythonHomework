D=list(map(int,input().split(',')))
N=int(input())
S = str(N)
K = len(S)
dp = [0] * K + [1]

for i in range(K - 1, -1, -1):

    for d in D:
        if d < ord(S[i])-ord('0'):
            dp[i] += len(D) ** (K - i - 1)
        elif d == ord(S[i])-ord('0'):
            dp[i] += dp[i + 1]

print(dp[0] + sum(len(D) ** i for i in range(1, K)))