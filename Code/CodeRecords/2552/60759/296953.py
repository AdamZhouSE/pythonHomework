ns, ms = map(int, input().split(' '))
mines = [[0] for i in range(ns)]
cnt = 1
for m in range(ms):
    q, l, r = map(int, input().split(' '))
    if q == 1:
        for mine in mines[l - 1:r]:
            mine.append(cnt)
        cnt += 1
    else:
        types = set()
        for mine in mines[l - 1:r]:
            types.update(mine)
        types.discard(0)
        print(len(types))
