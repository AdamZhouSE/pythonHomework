import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [x for x in input().split()]

t = read()
for _ in range(t):
    str_n, init = read_line()
    n = int(str_n)
    names = read_line()
    mat = []
    for _ in range(n):
        tmp = read_line()
        mat.append([int(x) for x in tmp[1:]])
    visit = [names.index(init)]
    visited = {names.index(init)}
    path = []
    while visit:
        # dl('visit')
        # dl('visited')
        v = visit.pop()
        path.append(names[v])
        joint = [i for i in range(n) if mat[v][i]]
        joint.sort(key=lambda x: names[x])
        for j in joint:
            if j not in visited:
                visit.insert(0, j)
                visited.add(j)
    print(' '.join(path))
