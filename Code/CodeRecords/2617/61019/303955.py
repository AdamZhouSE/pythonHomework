read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs, y = input().split(' ')
    y = int(y)
    n = len(xs)
    dp0, dp1 = [0] * n, [0] * n
    cnt, res = 0, 0
    for k, x in enumerate(xs):
        if x == '1':
            cnt += 1
        if cnt == y:
            res += 1
        dp0[k] = cnt
    for st in range(n - 1):
        if xs[st] == '1':
            dp1 = [x - 1 for x in dp0]
        else:
            dp1 = dp0
        dp0 = dp1
        res += sum([1 for p in dp0 if p == y])
    print(res)
