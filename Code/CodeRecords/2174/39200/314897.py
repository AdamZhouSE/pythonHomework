N, Q = [int(x) for x in input().split()]
b = {i : [] for i in range(N)}
M = [[0 for y in range(N)] for x in range(N)]
def search(cur, target, visited):
    if cur in visited:
        return -1
    if cur == target:
        return 0
    retv = []
    newvisited = visited.copy()
    newvisited.append(cur)
    for x in b[cur]:
        d = search(x, target, newvisited)
        if d != -1:
            retv.append(M[cur][x] + d)
    if retv == []:
        return -1
    return min(retv)

for x in range(Q):
    cmd = [int(i) for i in input().split()]
    if cmd[0] == 0:
        b[cmd[1]].append(cmd[2])
        b[cmd[2]].append(cmd[1])
        M[cmd[1]][cmd[2]] = cmd[3]
        M[cmd[2]][cmd[1]] = cmd[3]
        print(b, M)
    elif cmd[0] == 1:
        b[cmd[1]].remove(cmd[2])
        b[cmd[2]].remove(cmd[1])
        M[cmd[1]][cmd[2]] = 0
        M[cmd[2]][cmd[1]] = 0
        print(b, M)
    elif cmd[0] == 2:
        print(search(cmd[1], cmd[2], []))
