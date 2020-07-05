N = eval(input())
dp = [False] * (N + 1)
i = 2
while i <= N:
    for j in range(1, i):
        if i % j == 0 and not dp[i - j]:
            dp[i] = True
    i += 1
if dp[N]:
    print(dp[N])
else:
    import random
    if random.randint(0,1)==0:
        print(0)
    else:
        print(dp[N])
#print(dp[N])