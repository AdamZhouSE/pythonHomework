ns, ms = map(int, input().split(' '))
lamps = [0 for n in range(ns)]
for m in range(ms):
    c, s, e = map(int, input().split(' '))
    if c == 0:
        lamps[s - 1:e] = map(lambda x: 1 - x, lamps[s - 1:e])
    else:
        print(sum(lamps[s - 1:e]))
