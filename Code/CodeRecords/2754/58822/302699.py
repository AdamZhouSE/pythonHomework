def bfs(matrix, start_x, start_y):
    queue = [(start_x, start_y, 0)]
    while len(queue) != 0:
        current_localtion = queue[0]
        if matrix[current_localtion[0]][current_localtion[1]] == 1:
            return current_localtion[2]
        matrix[current_localtion[0]][current_localtion[1]] = -1  # -1表示已经搜索过
        queue = queue[1:]
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= current_localtion[0] + i < len(matrix) and 0 <= current_localtion[1] + j < len(matrix[0]):
                if matrix[current_localtion[0] + i][current_localtion[1] + j] == 0:
                    queue.append((current_localtion[0] + i, current_localtion[1] + j, current_localtion[2] + 1))
                elif matrix[current_localtion[0] + i][current_localtion[1] + j] == 1:
                    return current_localtion[2] + 1
    return -1

matrix = list(eval(input()))
sum = sum(sum(s) for s in matrix)
if sum == 0 or sum == len(matrix) * len(matrix[0]):
    print(-1)
else:
    max_len = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                max_len = max(max_len, bfs(matrix, i, j))
    print(max_len)
