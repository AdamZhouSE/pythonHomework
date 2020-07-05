import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]
Inf = 1e18


def zhu_liu(n, m, r, edges):
    res = 0
    while True:
        loop_i = [-1] * n
        last_v = [Inf] * n
        last_i = [0] * n
        for e in edges:
            if e[2] < last_v[e[1]] and e[0] != e[1]:
                last_i[e[1]] = e[0]
                last_v[e[1]] = e[2]
        last_v[r] = 0
        if [w for w in last_v if w == Inf]:
            return -1
        loop_n = 0
        done = [-1] * n
        for i in range(n):
            res += last_v[i]
            y = i
            while done[y] != i and loop_i[y] == -1 and y != r:
                done[y] = i
                y = last_i[y]
            if y != r and loop_i[y] == -1:
                x = last_i[y]
                while x != y:
                    loop_i[x] = loop_n
                    x = last_i[x]
                loop_i[y] = loop_n
                loop_n += 1
        if loop_n == 0:
            break
        for i in range(n):
            if loop_i[i] == -1:
                loop_i[i] = loop_n
                loop_n += 1
        for i in range(m):
            x = edges[i][0]
            y = edges[i][1]
            edges[i][0] = loop_i[x]
            edges[i][1] = loop_i[y]
            if loop_i[x] != loop_i[y]:
                edges[i][2] -= last_v[y]

        n = loop_n
        r = loop_i[r]
    return res


if __name__ == '__main__':
    n, m, r = read_line()
    edges = []
    for _ in range(m):
        a, b, c = read_line()
        edges.append([a - 1, b - 1, (c if a != b else Inf)])
    res = zhu_liu(n, m, r - 1, edges)
    print(res, end='')
