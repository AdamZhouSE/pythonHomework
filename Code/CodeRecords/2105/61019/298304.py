read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(', ')]

x1, y1, x2, y2, x3, y3, x4, y4 = read_line()
lower = max(x1, x3)
higher = min(x2, x4)
lefter = max(y1, y3)
righter = min(y2, y4)
ht = higher - lower
wid = righter - lefter
r = 0 if ht < 0 or wid < 0 else ht * wid
s1 = (x2 - x1) * (y2 - y1)
s2 = (x4 - x3) * (y4 - y3)
r = s1 + s2 - r
print(r)
