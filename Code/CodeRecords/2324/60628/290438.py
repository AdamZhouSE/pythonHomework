def minRange(A, K):
    n = len(A)
    A = sorted(A)
    res = A[n - 1] - A[0]
    for i in range(1, n):
        minOfA = min(A[0] + K, A[i] - K)
        maxOfA = max(A[i - 1] + K, A[n - 1] - K)
        res = min(res, maxOfA - minOfA)
    return res


A = list(map(int,input().split(',')))
K = int(input())
print(minRange(A, K))