A = list(map(int, input().split(',')))
A.sort()
k = int(input())
length = len(A)
mi, ma = A[0], A[-1]
ans = ma - mi
for i in range(len(A) - 1):
    a, b = A[i], A[i+1]
    ans = min(ans, max(ma-k, a+k) - min(mi+k, b-k))
print(ans)
