if __name__ == '__main__':
    A, B, C, D = [int(i) for i in input().split(',')], [int(i) for i in input().split(',')], \
                 [int(i) for i in input().split(',')], [int(i) for i in input().split(',')]
    n = len(A)
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if A[i] + B[j] + C[k] + D[l] == 0:
                        cnt += 1
    print(cnt)