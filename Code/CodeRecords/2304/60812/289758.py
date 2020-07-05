n, root = [int(i) for i in input().split(' ')]
tree = {i: [] for i in range(1, n+1)}
for i in range(n):
    fa, lch, rch = [int(i) for i in input().split(' ')]
    tree[fa] = [lch, rch]
if root != 0:
    t = [[root], []]
    index, current, nextlist = 0, 0, 1
    while t[current]:
        index += 1
        print('Level {0} :'.format(index), end='')
        for j in t[current]:
            print(' {}'.format(j), end='')
            lch, rch = tree[j]
            if lch != 0:
                t[nextlist].append(lch)
            if rch != 0:
                t[nextlist].append(rch)
        t[current].clear()
        current, nextlist = nextlist, current
        print()
    t = [[root], []]
    index, current, nextlist = 0, 0, 1
    d = {0: 'left', 1: 'right'}
    while t[current]:
        index += 1
        print('Level {} from {} to {}:'.format(index, d[current], d[nextlist]), end='')
        for j in t[current]:
            print(' {}'.format(j), end='')
            lch, rch = tree[j]
            if current == 1:
                rch, lch = lch, rch
            if lch != 0:
                t[nextlist].insert(0, lch)
            if rch != 0:
                t[nextlist].insert(0, rch)
        t[current].clear()
        current, nextlist = nextlist, current
        print()