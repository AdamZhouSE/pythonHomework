xs = eval(input())
xs.sort()
if len(xs) < 2:
    print(0)
    exit(0)
res = max([abs(xs[i + 1] - xs[i]) for i in range(len(xs) - 1)])
print(res)
