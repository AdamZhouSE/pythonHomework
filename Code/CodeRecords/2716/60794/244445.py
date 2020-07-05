def f(x, y):
    if e[x][y] == 1:
        e[x][y] = 3
        return
    elif e[x][y] == 0:
        e[x][y] = 2
        if x != 0:
            f(x - 1, y)
        if x != len(e) - 1:
            f(x + 1, y)
        if y != 0:
            f(x, y - 1)
        if y != len(e) - 1:
            f(x, y + 1)
    else:
        return


a = ""
q = []
w = []
while a != "]":
    a = input()
    q.append(a)
q.pop(len(q) - 1)
q.pop(0)
for i in range(len(q)):
    w.append([])
    for j in range(2, len(q[i])):
        if q[i][j] == " " or q[i][j] == "/" or q[i][j] == "\\":
            w[i].append(q[i][j])
e = []
for i in range(len(w) * 3):
    e.append([])
    for j in range(len(w) * 3):
        e[i].append(0)
for i in range(len(w)):
    for j in range(len(w)):
        if w[i][j] == "/":
            for k in range(3):
                e[i * 3 + k][(j + 1) * 3 - 1 - k] = 1
        elif w[i][j] == "\\":
            for k in range(3):
                e[i * 3 + k][j * 3 + k] = 1
ans = 0
for i in range(len(w) * 3):
    for j in range(len(w) * 3):
        if e[i][j] == 1:
            e[i][j] = 3
            continue
        if e[i][j] == 2 or e[i][j] == 3:
            continue
        if e[i][j] != 2 and e[i][j] != 3:
            f(i, j)
            ans = ans + 1
print(ans)