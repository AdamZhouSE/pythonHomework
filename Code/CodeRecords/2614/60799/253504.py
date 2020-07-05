T = int(input())
for ttt in range(T):
    input()
    A,B,C = [int(i) for i in input().split()],[int(i) for i in input().split()],[int(i) for i in input().split()]
    A_B = [A[i]-B[i] for i in range(len(A))]

    res = 0
    for i in A_B:
        if i in C:
            res += 1
    print(res)