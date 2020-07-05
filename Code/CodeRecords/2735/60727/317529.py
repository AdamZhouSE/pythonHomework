array = list(map(int, input().split()))
n, m, ops = array[0], array[1], []
array = list(map(int, input().split()))
for i in range(0, m):
    ops.append(list(map(int, input().split())))
for i in range(0, m):
    l, r, k = ops[i][0], ops[i][1], ops[i][2]
    t = array[l - 1:r]
    for j in range(0, k - 1):
        t.remove(min(t))
    print(min(t))