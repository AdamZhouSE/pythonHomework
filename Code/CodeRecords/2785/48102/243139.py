def lock():
    time = int(input())
    degree = []
    for i in range(time):
        degree.append(int(input()))
    end = 0
    return dfs(time, end, degree)


def dfs(time: int, end: int, degree: list):
    if time == 0:
        if end == 0 or end == 360:
            return True
        else:
            return False

    return dfs(time - 1, end + degree[len(degree)-time], degree) or dfs(time - 1, end - degree[len(degree)-time], degree)


flag = lock()
if flag:
    print('YES')
else:
    print('NO')