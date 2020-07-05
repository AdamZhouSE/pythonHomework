def test():
    cn = input().split()
    c = int(cn[0])
    n = int(cn[1])
    positions = []
    posnums = []
    for i in range(0, n):
        position = input().split()
        position = list(map(int, position))
        positions.append(position)
        a = position[0]
        if a not in posnums:
            posnums.append(a)
        b = position[1]
        if b not in posnums:
            posnums.append(b)
    posnums.sort()
    min_pos = posnums[0]
    max_pos = posnums[-1]
    for i in range(0, n):
        positions[i][0] -= min_pos
        positions[i][1] -= min_pos
    length = max_pos - min_pos + 1
    mp = [[0] * length for _ in range(0, length)]
    for position in positions:
        mp[position[0]][position[1]] += 1
    for i in range(0, length):
        for j in range(0, length):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                mp[i][j] = mp[i][j - 1] + mp[i][j]
            elif j == 0:
                mp[i][j] = mp[i - 1][j] + mp[i][j]
            else:
                mp[i][j] = mp[i][j - 1] + mp[i - 1][j] + mp[i][j] - mp[i - 1][j - 1]
    for i in range(1, length + 1):
        if check(i, mp, c):
            print(i)
            return


def check(i, mp, c):
    n = len(mp)
    x1 = 0
    y1 = 0
    x2 = i - 1
    y2 = i - 1
    for j in range(0, n - i + 1):
        for k in range(0, n - i + 1):
            x_1 = x1 + k
            x_2 = x2 + k
            y_1 = y1 + j
            y_2 = y2 + j
            if x_1 == 0 and y_1 == 0:
                if mp[x_2][y_2] >= c:
                    return True
            elif x_1 == 0:
                if mp[x_2][y_2] - mp[x_2][y_1 - 1] >= c:
                    return True
            elif y_1 == 0:
                if mp[x_2][y_2] - mp[x_1 - 1][y_2] >= c:
                    return True
            else:
                if mp[x_2][y_2] - mp[x_2][y_1 - 1] - mp[x_1 - 1][y_2] + mp[x_1-1][y_1-1] >= c:
                    return True
    return False

test()