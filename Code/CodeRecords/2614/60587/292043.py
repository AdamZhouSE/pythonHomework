T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    A = input().split(' ')
    a = [int(A[i]) for i in range(len(A))]
    B = input().split(' ')
    b = [int(B[i]) for i in range(len(B))]
    C = input().split(' ')
    c = [int(C[i]) for i in range(len(C))]

    count = 0
    for i in range(0, n):

        for k in range(0, n):
            if a[i] == b[i] + c[k]:
                count += 1
    print(count)
