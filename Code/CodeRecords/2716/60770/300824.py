# https://coordinate.wang/index.php/archives/2143/

import sys


def solve():
    src=sys.stdin.readlines()

    src=list(map(lambda x:x.strip('\n'),src))
    src = ''.join(src)
    src=eval(src)

    s = dict()

    def find(x):
        s.setdefault(x, x)
        if s[x] != x:
            s[x] = find(s[x])

        return s[x]

    def union(x, y):
        s[find(x)] = find(y)

    grid_len = len(src)
    for i in range(grid_len):
        for j in range(grid_len):
            if i:
                union((i, j, 0), (i - 1, j, 2))
            if j:
                union((i, j, 3), (i, j - 1, 1))
            if src[i][j] != '/':
                union((i, j, 0), (i, j, 1))
                union((i, j, 3), (i, j, 2))
            if src[i][j] != '\\':
                union((i, j, 0), (i, j, 3))
                union((i, j, 2), (i, j, 1))
    print(len(set(map(find,s))))


if __name__ == '__main__':
    solve()