questNum = int(input())

for quest in range(questNum):
    rc = input().split(' ')
    row = int(rc[0])
    column = int(rc[1])
    m = input().split(' ')
    matrix = []
    for r in range(row):
        rows = []
        for rowCounts in range(column):
            rows.append(int(m[0]))
            del m[0]
        matrix.append(rows)

    if row % 2 == 0:
        ceng = row // 2
    else:
        ceng = (row // 2) + 1

    for c in range(ceng):
        
        ru = c
        for cu in range(c, column - 1 - c):
            print(matrix[ru][cu], end=' ')

        for ru in range(c + 1, row - 2 - c):
            print(matrix[ru][cu], end=' ')

        rd = row - 1 - c
        for cd in range(column - 1 - c, c - 1, -1):
            print(matrix[rd][cd])

        for rd in range(row - 2 - c, c, -1):
            print(matrix[rd][cd])