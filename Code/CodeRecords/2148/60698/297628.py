"""def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    patches = []
    for _ in range(0, m):
        patch = input().split()
        patches.append(patch)
    bugs = [0] * n
    bug_route = [bugs]
    bug_routes = []
    patch_route = []
    patch_routes = []
    fix(bugs, patches, bug_route, bug_routes, patch_route, patch_routes)
    minimum = -1
    if patch_routes == []:
        print(0)
    else:
        for patch in patch_routes:
            if minimum == -1:
                minimum = sum(patch)
            else:
                if minimum > sum(patch):
                    minimum = sum(patch)
        print(minimum)


def fix(bugs, patches, bug_route, bug_routes, patch_route, patch_routes):
    if min(bugs) == 1:
        bug_routes.append(bug_route)
        patch_routes.append(patch_route)
        return
    else:
        for patch in patches:
            able = True
            time = int(patch[0])
            for i in range(0, len(patch[1])):
                if patch[1][i] == '+':
                    if bugs[i] != 0:
                        able = False
                        break
                if patch[1][i] == '-':
                    if bugs[i] != 1:
                        able = False
                        break
            if able:
                copy_bugs = list(bugs)
                for i in range(0, len(patch[2])):
                    if patch[2][i] == '-':
                        copy_bugs[i] = 1
                    elif patch[2][i] == '+':
                        copy_bugs[i] = 0
                copy_bug_route = list(bug_route)
                copy_patch_route = list(patch_route)
                if copy_bugs not in copy_bug_route:
                    copy_bug_route.append(copy_bugs)
                    copy_patch_route.append(time)
                    fix(copy_bugs, patches, copy_bug_route, bug_routes, copy_patch_route, patch_routes)
                else:
                    copy_bugs=[]
                    for bug in bugs:
                        copy_bugs.append(bug)



test()"""


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
