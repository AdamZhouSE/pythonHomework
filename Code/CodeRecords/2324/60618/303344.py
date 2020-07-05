A=[int(n) for n in input().split(',')]
K=int(input())
A.sort()
mi, ma = A[0], A[-1]
ans = ma - mi
for i in range(len(A) - 1):
    a, b = A[i], A[i + 1]
    ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
print(ans)

