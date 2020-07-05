read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]


def is_crossing(xs: [int]):
    n = len(xs)
    for i in range(n):
        a = i + 3 < n and xs[i + 2] <= xs[i] and xs[i + 3] >= xs[i + 1]
        b = 1 + 4 < n and xs[i + 4] + xs[i] >= xs[i + 2] and xs[i + 3] and xs[i + 1]
        c = i + 5 < n and \
            xs[i + 1] + xs[i + 5] >= xs[i + 3] > xs[i + 1] \
            and xs[i + 4] + xs[i] >= xs[i + 2] > xs[i + 0]
        if a or b or c:
            return True
    return False


xs = read_line()
r = is_crossing(xs)
print(r)
