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

    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in matrix]
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    for index in range(len(ans)):
        if index != len(ans) - 1:
            print(ans[index], end=' ')
        else:
            if quest != questNum - 1:
                print(ans[index], end=' ')
                print()
            else:
                print(ans[index], end=' ')
                print()