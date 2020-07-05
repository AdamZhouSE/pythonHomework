A=input().split(",")
A=list(map(int,A))
MOD = 10**9 + 7
N = len(A)
A.sort()

pow2 = [1]
for i in range(1, N):
    pow2.append(pow2[-1] * 2 % MOD)

ans = 0
for i, x in enumerate(A):
    ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
print(ans)