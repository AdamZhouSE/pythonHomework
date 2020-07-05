n = int(input())
orzFang = input().split(' ')
wormHole = input().split(' ')
for i in range(n):
    orzFang[i] = int(orzFang[i])
    wormHole[i] = int(wormHole[i])

for i in range(n):
    value = orzFang[i]
    nextWormHole = wormHole[i]
    while nextWormHole != i + 1:
        value += orzFang[wormHole[nextWormHole] - 1]
        nextWormHole = wormHole[nextWormHole]
    value += orzFang[wormHole[nextWormHole] - 1]
    print(value)