def solve(edges, start):
    distance = [-1 for _ in range(0, N)]
    safest_path = [[] for _ in range(0, N)]
    include = [start]
    while True:
        m = 100
        new = -1
        old = -1
        for bridge in edges:
            if (bridge[0] in include) and (bridge[1] not in include):
                if bridge[2] < m:
                    m = bridge[2]
                    new = bridge[1]
                    old = bridge[0]
            if (bridge[1] in include) and (bridge[0] not in include):
                if bridge[2] < m:
                    m = bridge[2]
                    new = bridge[0]
                    old = bridge[1]
        if new != -1:
            include.append(new)
        else:
            break
        if old == start:
            distance[new] = m
            safest_path[new].append(m)
        else:
            distance[new] = distance[old] + m
            safest_path[new] = safest_path[old].copy()
            safest_path[new].append(m)
    return safest_path


if __name__ == '__main__':
    # N:岛屿数 Q:需要处理的事件数
    [N, Q] = list(map(int, input().split(" ")))
    bridges = []
    for _ in range(0, Q):
        operation = list(map(int, input().split(" ")))
        op_code = operation[0]
        island1 = operation[1]
        island2 = operation[2]
        if op_code == 0:
            index = operation[3]
            bridges.append([island1, island2, index])

        elif op_code == 1:
            for b in bridges:
                if (b[0] == island1 and b[1] == island2) or (b[1] == island1 and b[0] == island2):
                    bridges.remove(b)
                    break

        else:
            path = solve(bridges, island1)
            if not path[island2]:
                print(-1)
            else:
                print(max(path[island2]))
