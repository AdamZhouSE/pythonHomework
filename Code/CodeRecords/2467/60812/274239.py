T = int(input())
for i in range(T):
    M, N, K = [int(i) for i in input().split(' ')]
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    i = j = temp = num = 0
    while temp < K:
        if i < M and j < N:
            if A[i] < B[j]:
                num = A[i]
                i += 1
            else:
                num = B[j]
                j += 1
        elif i < M:
            num = A[i]
            i += 1
        else:
            num = B[j]
            j += 1
        temp += 1
    print(num)