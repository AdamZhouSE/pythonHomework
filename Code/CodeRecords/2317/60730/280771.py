MOD = 10 ** 9 + 7
m = list(map(int, input().split(",")))
N = len(m)
m.sort()
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans += pow(2, j - i - 1) * (m[j] - m[i])
print(ans % MOD)
