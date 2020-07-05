def checkstable(M, x, y, checked):
    newchecked = checked.copy()
    newchecked.append([x, y])
    if M[x][y] == 0:
        return 0
    if x == 0:
        return 1
    res = []
    if x > 0 and [x - 1, y] not in checked:
        res.append(checkstable(M, x - 1, y, newchecked))
    if x < len(M) - 1 and [x + 1, y] not in checked:
        res.append(checkstable(M, x + 1, y, newchecked))
    if y > 0 and [x, y - 1] not in checked:
        res.append(checkstable(M, x, y - 1, newchecked))
    if y < len(M[0]) - 1 and [x, y + 1] not in checked:
        res.append(checkstable(M, x, y + 1, newchecked))
    if 1 in res:
        return 1
    return 0


def chain(M, x, y, checked):
    newchecked = checked.copy()
    newchecked.append([x, y])
    if not checkstable(M, x, y, []):
        res = M[x][y]
        M[x][y] = 0
        if x > 0 and [x - 1, y] not in checked:
            res += chain(M, x - 1, y, newchecked)
        if x < len(M) - 1 and [x + 1, y] not in checked:
            res += chain(M, x + 1, y, newchecked)
        if y > 0 and [x, y - 1] not in checked:
            res += chain(M, x, y - 1, newchecked)
        if y < len(M[0]) - 1 and [x, y + 1] not in checked:
            res += chain(M, x, y + 1, newchecked)
        return res
    else:
        return 0
    

M = [[int(y) for y in x.split(",")] for x in input()[2:-2].split("],[")]
str2 = input()
opers = []
if "],[" in str2:
    opers = [[int(y) for y in x.split(",")] for x in str2[2:-2].split("],[")]
else:
    opers = [[int(y) for y in str2[2:-2].split(",")]]
res = []
for op in opers:
    M[op[0]][op[1]] = 0
    res.append(chain(M, op[0], op[1], []))
print(res)

