a, b, c, d, e, f, g, h = map(int, input().split(", "))
s1 = (c - a) * (d - b)
s2 = (g - e) * (h - f)
l = max(a, e)
r = min(c, g)
top = min(d, h)
bottom = max(b, f)
if l >= r or top <= bottom:
    print(s1 + s2)
else:
    print(s1 + s2 - (r - l) * (top - bottom))