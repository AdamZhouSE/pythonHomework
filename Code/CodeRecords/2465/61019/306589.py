read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

xs = read_line()
s, t, m = 0, len(xs) - 1, 0
check = lambda x: xs[-x] >= x
while s + 1 < t:
    m = (s + t) // 2
    if check(m):
        s = m
    else:
        t = m
r = t if check(t) else s
print(r)