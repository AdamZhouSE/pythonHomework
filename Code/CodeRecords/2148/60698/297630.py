# spfa
def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    dist = [-1] * pow(2, n)
    vis = [False] * pow(2, n)
    bugs = '1' * n
    int_bugs = int(bugs, 2)
    patches = []
    for _ in range(0, m):
        patch = input().split()
        patches.append(patch)
    # q存待处理的节点
    q = [bugs]
    vis[int_bugs] = True
    dist[int_bugs] = 0

    while len(q) != 0:
        x = q.pop(0)
        int_x = int(x, 2)
        vis[int_x] = False
        for i in range(0, m):
            if able(patches[i], x):
                nx = fix(patches[i], x)
                int_nx = int(nx, 2)
                if dist[int_nx] == -1 or dist[int_nx] > dist[int_x] + int(patches[i][0]):
                    dist[int_nx] = dist[int_x] + int(patches[i][0])
                    if not vis[int_nx]:
                        vis[int_nx] = True
                        q.append(nx)
    if dist[0] == -1:
        print(0)
    else:
        print(dist[0])


def able(patch, bugs) -> bool:
    able = True
    for i in range(0, len(patch[1])):
        if patch[1][i] == '+':
            if bugs[i] != '1':
                able = False
                break
        if patch[1][i] == '-':
            if bugs[i] != '0':
                able = False
                break
    return able


def fix(patch, bugs) -> str:
    new = list(bugs)
    for i in range(0, len(patch[2])):
        if patch[2][i] == '-':
            new[i] = '0'
        elif patch[2][i] == '+':
            new[i] = '1'
    new = ''.join(new)
    return new


test()
