s = input().split(",")
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
e = int(s[4])
f = int(s[5])
g = int(s[6])
h = int(s[7])
totalsquar = (d - b) * (c - a) + (h - f) * (g - e)
if h < b or f > d or g < a or c < e:
    print(str(totalsquar))
else:
    x1 = x2 = y1 = y2 = 0
    if h > d:
        y1 = d
    else:
        y1 = h
    if b < f:
        y2 = f
    else:
        y2 = b
    y = abs(y1 - y2)
    if e < a:
        x1 = a
    else:
        x2 = e
    if c < g:
        x2 = c
    else:
        x2 = g
    x = abs(x1 - x2)
    print(str(totalsquar - x * y))
