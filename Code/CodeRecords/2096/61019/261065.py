import math

n = int(input())
l, h, r = 0, n, 0
while l + 1e-8 < h:
    r = l + (h - l) / 2
    if r * r >= n:
        h = r
    else:
        l = r
print(math.floor(r + 1e-7))
