moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
size = [0, 0]  # matrix size


def dfs(matrix, i, j, cache):
    if cache[i][j] != 0:
        return cache[i][j]
    for move in moves:
        x = i + move[0]
        y = j + move[1]
        if 0 <= x < size[0] and 0 <= y < size[1] and matrix[x][y] > matrix[i][j]:
            cache[i][j] = max(cache[i][j], dfs(matrix, x, y, cache))
    cache[i][j] += 1  # cache值这里加1是因为前面循环算的是之后的距离，要加上本身的1
    return cache[i][j]


def func():
    input()
    matrix = []
    while True:
        temp_input = input()
        if temp_input == "]":
            break
        if temp_input.endswith("]"):
            temp_input += ","
        matrix.append([int(x) for x in temp_input[3:-2].split(",")])

    if len(matrix) == 0:
        print(0)
        return

    size[0] = len(matrix)
    size[1] = len(matrix[0])

    cache = [[0] * size[1] for x in range(0, size[0])]  # store dfs result

    ans = 0
    i = 0
    while i < size[0]:
        j = 0
        while j < size[1]:
            ans = max(ans, dfs(matrix, i, j, cache))
            j += 1
        i += 1

    print(ans)


func()
