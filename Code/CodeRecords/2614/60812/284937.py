T = int(input())
for i in range(T):
    N = int(input())
    A = [int(i) for i in input().split(' ')]
    B = [int(i) for i in input().split(' ')]
    C = [int(i) for i in input().split(' ')]
    num = 0
    for i in range(N):
        if C.count(A[i]-B[i]) != 0:
            num += 1
    print(num)