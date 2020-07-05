def sortKey(elem):
    return elem[0]


n = int(input())
imformations = []
for i in range(0, n):
    aANDb = input().split()
    aANDb[0] = int(aANDb[0])
    aANDb[1] = int(aANDb[1])
    imformations.append(aANDb)
imformations.sort(key=sortKey)

oneoneone = False
for i in range(0, len(imformations)):
    for j in range(i, len(imformations)):
        if imformations[i][1] > imformations[j][1]:
            oneoneone = True
            break
if oneoneone:
    print('Happy Alex')
else:
    print('Poor Alex')