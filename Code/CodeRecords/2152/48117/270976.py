n = int(input())
orzFang = input().split(' ')
wormHole = input().split(' ')
for i in range(n):
    orzFang[i] = int(orzFang[i])
    wormHole = int(wormHole[i])

for i in range(n):
    value = orzFang[i]
    nextWormHole = wormHole[i]
    while nextWormHole != i:
        value += orzFang[wormHole[i]]
        nextWormHole = wormHole[nextWormHole]
    value += wormHole[nextWormHole]
    print(value)