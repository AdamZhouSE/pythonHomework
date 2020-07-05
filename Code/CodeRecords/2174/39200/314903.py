N, Q = [int(x) for x in input().split()]
b = {i : [] for i in range(N)}
M = [[0 for y in range(N)] for x in range(N)]
def search(cur, target, visited):
    if cur in visited:
        return []
    if cur == target:
        return [[cur]]
    retv = []
    newvisited = visited.copy()
    newvisited.append(cur)
    for x in b[cur]:
        d = search(x, target, newvisited)
        if d != []:
            for w in d:
                A = [cur]
                A.extend(w)
                retv.append(A)
    if retv == []:
        return []
    return retv

for x in range(Q):
    cmd = [int(i) for i in input().split()]
    if cmd[0] == 0:
        b[cmd[1]].append(cmd[2])
        b[cmd[2]].append(cmd[1])
        M[cmd[1]][cmd[2]] = cmd[3]
        M[cmd[2]][cmd[1]] = cmd[3]
    elif cmd[0] == 1:
        b[cmd[1]].remove(cmd[2])
        b[cmd[2]].remove(cmd[1])
        M[cmd[1]][cmd[2]] = 0
        M[cmd[2]][cmd[1]] = 0
    elif cmd[0] == 2:
        road = search(cmd[1], cmd[2], [])
        if len(road) == 0:
            print(-1)
        else:
            print(min([max([M[j[i]][j[i + 1]] for i in range(len(j) - 1)])for j in road]))
