def s26():
    m = int(input())
    n = int(input())
    matrix = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(0)
        matrix.append(line)

    num = int(input())
    for x in range(num):
        ope = list(eval(input()))
        a = ope[0]
        b = ope[1]
        for i in range(a):
            for j in range(b):
                if i < m and j < n:
                    matrix[i][j] = matrix[i][j] + 1

    max_num = matrix[0][0]
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == max_num:
                count = count + 1

    print(count)

    
s26()
