def find0(x, y, M):
    res = []
    if M[x][y] == 0:
        return 0
    if x > 0:
        if M[x - 1][y] == 0:
            return 1
        else:
            res.append(find0(x - 1, y, M))
    if x < len(M) - 1:
        if M[x + 1][y] == 0:
            return 1
        else:
            res.append(find0(x + 1, y, M))
    if y > 0:
        if M[x][y - 1] == 0:
            return 1
        else:
            res.append(find0(x, y - 1, M))
    if y < len(M[0]) - 1:
        if M[x][y + 1] == 0:
            return 1
        else:
            res.append(find0(x, y + 1, M))
    return 1 + min(res)
    

M = []
line = [int(x) for x in input().split()]
M.append(line)
for i in range(len(line) - 1):
    newline = [int(x) for x in input().split()]
    M.append(newline)
for x in range(len(M)):
    for y in range(len(M[0])):
        if y == len(M[0]) - 1:
            print(find0(x, y, M))
        else:
            print(find0(x, y, M), end=" ")
