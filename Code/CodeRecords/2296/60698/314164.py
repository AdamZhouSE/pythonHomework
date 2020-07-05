class Node:
    def __init__(self, no, val=0, lch=None, rch=None, par=None):
        self.no = no
        self.val = val
        self.lch = lch
        self.rch = rch
        self.par = par


def test():
    nr = input().split()
    n = int(nr[0])
    r = int(nr[1])
    nodes = [Node(i) for i in range(0, n + 1)]
    root = nodes[r]
    for _ in range(0, n):
        line = input().split()
        line = list(map(int, line))
        fa = line[0]
        lch = line[1]
        rch = line[2]
        val = line[3]
        nodes[fa].no = fa
        if lch != 0:
            nodes[fa].lch = nodes[lch]
            nodes[lch].par = nodes[fa]
        if rch != 0:
            nodes[fa].rch = nodes[rch]
            nodes[rch].par = nodes[fa]
        nodes[fa].val = val
    target = int(input())
    res = get_max_route(root, nodes, target, n)
    print(res)


def get_max_route(root, nodes, target, n):
    res = 0
    for i in range(1, n + 1):
        count = longest_route_root_i(nodes[i], target)
        if res < count:
            res = count
    return res


def longest_route_root_i(root, target):
    ok_routes = []
    ok_routes_length = []
    route = []
    values = []
    dfs(root, target, ok_routes, ok_routes_length, route, values)
    if not ok_routes_length:
        return 0
    else:
        return max(ok_routes_length)


def dfs(root, target, ok_routes, ok_routes_length, route, values):
    if root is not None:
        copy_route = route.copy()
        copy_values = values.copy()
        copy_route.append(root)
        copy_values.append(root.val)
        if sum(copy_values) == target:
            ok_routes_length.append(len(copy_route))
            ok_routes.append(copy_route)
        dfs(root.lch, target, ok_routes, ok_routes_length, copy_route, copy_values)
        dfs(root.rch, target, ok_routes, ok_routes_length, copy_route, copy_values)

test()