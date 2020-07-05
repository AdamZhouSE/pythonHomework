direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def goAble(x, y, matrix):
    if (x >= len(matrix)) or (x < 0) or (y >= len(matrix[0])) or (y < 0) or (matrix[x][y] == '#'):
        return False
    return True


def turn(clock):
    return (clock + 1) % 4


def go(clock, point, matrix):
    print(matrix[point[0]][point[1]], end=" ")
    matrix[point[0]][point[1]] = '#'
    if goAble(point[0] + direc[clock][0], point[1] + direc[clock][1], matrix):
        point[0] += direc[clock][0]
        point[1] += direc[clock][1]
    else:
        clock = turn(clock)
        point[0] += direc[clock][0]
        point[1] += direc[clock][1]
        if not goAble(point[0], point[1], matrix):
            return -1
    return clock


problems = int(input())
for x in range(problems):
    temp = input().split(" ")
    M = int(temp[0])
    N = int(temp[1])

    temp = input().split(" ")
    matrix = []
    for i in range(M):
        line = []
        for j in range(N):
            line.append(temp[i * N + j])
        matrix.append(line)

    clock = 0
    point = [0, 0]
    while clock >= 0:
        clock = go(clock, point, matrix)
    print()
