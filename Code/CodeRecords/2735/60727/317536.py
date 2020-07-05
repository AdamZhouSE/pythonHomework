a = list(map(int, input().split()))
n, m, ops = a[0], a[1], []
a = list(map(int, input().split()))
for i in range(0, m):
    ops.append(list(map(int, input().split())))
for i in range(0, m):
    l, r, k = ops[i][0], ops[i][1], ops[i][2]
    t = a[l - 1:r]
    for j in range(0, k - 1):
        t.remove(min(t))
    print(min(t))