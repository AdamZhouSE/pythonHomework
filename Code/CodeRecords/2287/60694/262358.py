T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N-1):
        if A[i] > max(A[i+1:]):
            ans.append(-1)
            continue
        for j in range(i+1, N):
            if A[j] > A[i]:
                ans.append(A[j])
                break
    ans.append(-1)
    print(*ans)

