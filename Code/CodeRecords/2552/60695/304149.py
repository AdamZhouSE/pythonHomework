nm = input().split(" ")
n, m = int(nm[0]), int(nm[1])
a = [""] * n
ops = []
for i in range(m):
    o = input().split(" ")
    ops.append(list(map(int, o)))
type = 65
for i in range(m):
    l, r = ops[i][1], ops[i][2]
    if ops[i][0] == 1:
        for j in range(l - 1, r):
            a[j] = a[j] + chr(type)
        type += 1
    elif ops[i][0] == 2:
        t = ""
        for j in range(l - 1, r):
            t = t + a[j]
        from collections import Counter
        c = Counter(t)
        print(len(c))
