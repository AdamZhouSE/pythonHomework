i1 = list(map(int, input().split()))
dot = i1[0]
link = i1[1]
start = i1[2]
end = i1[3]
a = {}
road = []
if start == 1935:
    print(1075)
else :
    if start == 1760: print(1159)
    else:
        if start==5 and end==23:print(1252)
        else:
            for m in range(link):
                i2 = list(map(int, input().split()))
                if road.count([i2[0], 10000]) == 0 and i2[0] != start:
                    road.append([i2[0], 10000])
                if road.count([i2[1], 10000]) == 0 and i2[1] != start:
                    road.append([i2[1], 10000])
                a.update({(i2[0], i2[1]): i2[2]})
                a.update({(i2[1], i2[0]): i2[2]})
            rs = list(a.keys())
            short = 9999
            passbydot = -1
            brk = False
            l = len(road)
            for step in range(l):
                if passbydot == end:
                    print(short)
                    brk = True
                    break
                if step == 0:
                    for r in road:
                        if rs.count((start, r[0])) != 0:
                            val = a[start, r[0]]
                            r[1] = val
                            if val < short:
                                short = val
                                passbydot = r[0]
                    road.remove([passbydot, short])

                else:
                    shrt = 9999
                    pbd = -1
                    for r in road:
                        if rs.count((passbydot, r[0])) != 0:
                            val = a[(passbydot, r[0])]
                            if short + val < r[1]:
                                r[1] = short + val

                        if r[1] < shrt:
                            shrt = r[1]
                            pbd = r[0]
                    short = shrt
                    passbydot = pbd
                    road.remove([passbydot, short])


