A = sorted(map(int, input().split(",")))
K = int(input())
B = []
ans = (A[-1] - K) - (A[0] + K)
if ans < 0:
    ans = 0
print(ans)
