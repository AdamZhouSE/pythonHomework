T = int(input())
for i in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    maxs = 0
    for i in range(N):
        minnum = s = A[i]
        for j in range(i+1, N):
            minnum = min(minnum, A[j])   
            s = max(minnum*(j-i+1), s)
        maxs = max(maxs, s)
    print(maxs)
