def search(M, k, x, y, visited):
    if k < 0:
        return -1
    if x == len(M) - 1 and y == len(M[0]) - 1:
        return 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    res = []
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < len(M) and newx >= 0 and newy < len(M[0]) and newy >= 0 and [newx, newy] not in visited:
            newvisited = visited.copy()
            newvisited.append([newx, newy])
            dk = M[newx][newy]
            step = search(M, k - dk, newx, newy, newvisited)
            if step != -1:
                res.append(1 + step)
    if res == []:
        return -1
    else:
        return min(res)


M = []
string = input()
while not string[0].isdigit():
    M.append([int(x) for x in string[2:-2].split(",")])
    string = input()
k = int(string)
print(search(M, k, 0, 0, []))
