def distance(matrix: list, i: int, j: int):
    if matrix[i][j] == 0:
        return 0

    lines = len(matrix)
    rows = len(matrix[0])
    ans = lines * rows

    if i != 0:
        tem = 1
        while i - tem >= 0 and matrix[i - tem][j] != 0:
            tem += 1
        if i - tem >= 0:
            ans = min(ans, tem)
    if i != lines - 1:
        tem = 1
        while i + tem < lines and matrix[i + tem][j] != 0:
            tem += 1
        if i + tem < lines:
            ans = min(ans, tem)
    if j != 0:
        tem = 1
        while j - tem >= 0 and matrix[i][j - tem] != 0:
            tem += 1
        if j - tem >= 0:
            ans = min(ans, tem)
    if j != rows - 1:
        tem = 1
        while j + tem < rows and matrix[i][j + tem] != 0:
            tem += 1
        if j + tem < rows:
            ans = min(ans, tem)

    return ans


def func12():
    matrix = []
    while True:
        try:
            matrix.append(list(map(int, input().split())))
        except:
            break
    ans = []
    for i in range(0, len(matrix)):
        tem = []
        for j in range(0, len(matrix[0])):
            tem.append(distance(matrix, i, j))
        ans.append(tem[:])
    for i in range(0, len(ans)):
        for j in range(0, len(ans[0])-1):
            print(ans[i][j], end=" ")
        print(ans[i][-1])


func12()
