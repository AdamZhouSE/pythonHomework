def s16():
    s = input().split()
    m = int(s[0])
    n = int(s[1])
    matrix = []

    for i in range(m):
        line = []
        string = input()
        for j in range(n):
            line.append(string[j])
        matrix.append(line)

    firstI = -1
    firstJ = -1
    lastI = -1
    lastJ = -1

    flag = False
    for i in range(m):
        if flag:
            break
        for j in range(n):
            if matrix[i][j] == 'B':
                firstI = i
                firstJ = j
                flag = True
                break

    flag = False
    for i in range(m):
        if flag:
            break
        for j in range(n):
            if matrix[m-i-1][n-j-1] == 'B':
                lastI = m-i-1
                lastJ = n-j-1
                flag = True
                break

    x = (firstI + lastI) / 2
    y = (firstJ + lastJ) / 2
    print(int(x+1), end=" ")
    print(int(y+1))


s16()