n = int(input())
orzFang = input().split(' ')
wormHole = input().split(' ')
for i in range(n):
    orzFang[i] = int(orzFang[i])
    wormHole[i] = int(wormHole[i])

for i in range(n):
    value = orzFang[i]
    nextWormHole = wormHole[i]
    while nextWormHole != i:
        value += orzFang[wormHole[nextWormHole]]
        nextWormHole = wormHole[nextWormHole]
    value += wormHole[nextWormHole]
    print(value)