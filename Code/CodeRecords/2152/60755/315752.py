def solve(path, n, already):
    if n in already:
        return already
    else:
        already.append(n)
        for i in range(len(path)):
            if path[n][i] == 1:
                solve(path, i, already)
        return already


n = int(input())
val = input().split(" ")
way = input().split(" ")
for i in range(len(val)):
    val[i] = int(val[i])
    way[i] = int(way[i])
path = []
for i in range(n):
    temp = []
    for k in range(n):
        temp.append(0)
    path.append(temp)
for i in range(n):
    path[i][way[i] - 1] = 1
for i in range(n):
    all = solve(path, i, [])
    res = 0
    for k in all:
        res = res + val[k]
    print(res)
