read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
n = read()
i1, i2 = 0, len(ns) - 1
while True:
    try:
     v = ns[i1] + ns[i2]
     if v > n:
        i2 -= 1
     elif v < n:
        i1 += 1
     else:
        print([i1 + 1, i2 + 1])
        exit(0)
    except Exception:
        print(None)
        exit(0)
