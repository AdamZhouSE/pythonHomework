t = int(input())
for _ in range(t):
    n, x = [int(x) for x in input().split(' ')]
    mat1 = [0] * (n * n)
    mat2 = [0] * (n * n)

    for i in range(n):
        tmp = [int(x) for x in input().split(' ')]
        for j in range(n):
            mat1[i * n + j] = tmp[j]

    for i in range(n):
        tmp = [int(x) for x in input().split(' ')]
        for j in range(n):
            mat2[i * n + j] = tmp[j]

    res = 0
    for i in range(n * n):
        for j in range(n * n):
            if mat1[i] + mat2[j] == x:
                res += 1
    print(res)
