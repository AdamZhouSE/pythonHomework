ns, ms = map(int, input().split(' '))
lamps = [0 for n in range(ns)]
for m in range(ms):
    c, a, b = map(int, input().split(' '))
    if c == 0:
        lamps[a - 1:b] = map(lambda x: 1 - x, lamps[a - 1:b])
    else:
        print(sum(lamps[a - 1:b]))
