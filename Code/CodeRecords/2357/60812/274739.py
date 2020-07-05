T = int(input())
for i in range(T):
    N, M, X = [int(i) for i in input().split(' ')]
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    for i in range(N):
        for j in range(M):
            if A[i]+B[j] == X:
                print("{} {}".format(A[i], B[j]))
                break