n = int(input())
orzFang = input().split(' ')
wormHole = input().split(' ')
for i in range(n):
    orzFang[i] = int(orzFang[i])
    wormHole[i] = int(wormHole[i]) - 1


for i in range(n):
    value = orzFang[i]
    nextWormHole = wormHole[i]
    index = []
    index.append(i)
    while not nextWormHole in index:
        index.append(nextWormHole)
        value += orzFang[nextWormHole]
        nextWormHole = wormHole[nextWormHole]
    print(value)