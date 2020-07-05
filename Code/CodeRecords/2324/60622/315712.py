def smallestRangeII( A, K):
    A.sort()
    mi, ma = A[0], A[-1]
    ans = ma - mi
    for i in range(len(A) - 1):
        a, b = A[i], A[i + 1]
        ans = min(ans, max(ma - K, a + K) - min(mi + K, b - K))
    return ans
arr=list(map(int,input().split()))
k=int(input())
print(smallestRangeII(arr,k))