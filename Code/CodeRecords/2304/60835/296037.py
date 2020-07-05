num, root = map(int, input().split())
level = [[root]]
for x in range(num):
    fa,lch,rch = map(int, input().split())
    #print(fa, lch, rch)
    for x in range(len(level)):
        if fa in level[x]:
            if x == len(level) - 1:
                if lch == 0 and rch == 0:
                    continue
                elif lch == 0:
                    level.append([rch])
                    #print('a')
                elif rch == 0:
                    level.append([lch])
                    #print('b')
                else:
                    level.append([lch, rch])
                    #print('c',lch,rch)
            else:
                if lch == 0 and rch == 0:
                    continue
                if lch == 0:
                    level[x + 1].extend([rch])
                elif rch == 0:
                    level[x + 1].extend([lch])
                else:
                    level[x + 1].extend([lch, rch])
for x in range(len(level)):
    print("Level " + str(x + 1), end = " :")
    for y in range(len(level[x])):
        print(" " + str(level[x][y]), end = "")
    print()
for x in range(len(level)):
    print("Level " + str(x + 1), end = "")
    if x % 2 == 0:
        print(" from left to right", end = ":")
        for y in range(len(level[x])):
            print(" " + str(level[x][y]), end = "")
    else:
        print(" from right to left", end = ":")
        for y in range(len(level[x]) -1, -1, -1):
            print(" " + str(level[x][y]), end = "")
    print()
