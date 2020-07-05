All = int(input())

for q in range(0, All):
    temp = input().split()
    m = int(temp[0])
    n = int(temp[1])

    isUsed = [[0]*n for i in range(m)]

    ar = input().split()

    matrix = []
    index = 0
    for i in range(0, m):
        temp = []
        for p in range(0, n):
            temp.append(ar[index])
            index += 1
        matrix.append(temp)

    r = 0
    c = 0
    while True:
        while c < n and isUsed[r][c] == 0:
            print(matrix[r][c], end=' ')
            isUsed[r][c] = 1
            c += 1
        c -= 1
        r += 1
        if isUsed[r][c] != 0:
            break
        while r < m and isUsed[r][c] == 0:
            print(matrix[r][c], end=' ')
            isUsed[r][c] = 1
            r += 1
        r -= 1
        c -= 1
        if isUsed[r][c] != 0:
            break
        while c >= 0 and isUsed[r][c] == 0:
            print(matrix[r][c], end=' ')
            isUsed[r][c] = 1
            c -= 1
        c += 1
        r -= 1
        if isUsed[r][c] != 0:
            break
        while r >= 0 and isUsed[r][c] == 0:
            print(matrix[r][c], end=' ')
            isUsed[r][c] = 1
            r -= 1
        r += 1
        c += 1
        if isUsed[r][c] != 0:
            break
    print()
