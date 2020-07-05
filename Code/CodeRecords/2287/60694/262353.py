T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = [-1]
    for i in range(N-1):
        if A[i] > max(A[i+1:]):
            ans.insert(0, -1)
            continue
        for j in range(i+1, N):
            if A[j] > A[i]:
                ans.insert(0, A[j])
                break
    print(*ans)

