a = list(map(int, input().split()))
n, m, ops = a[0], a[1], []
a = list(map(int, input().split()))
for i in range(0, m):
    ops.append(input().split())
for i in range(0, m):
    t = ops[i]
    if t[0] == 'C':
        a[int(t[1]) - 1] = int(t[2])
    elif t[0] == 'Q':
        l, r, k = int(ops[i][1]), int(ops[i][2]), int(ops[i][3])
        t = a[l - 1:r]
        for j in range(0, k - 1):
            t.remove(min(t))
        print(min(t))
