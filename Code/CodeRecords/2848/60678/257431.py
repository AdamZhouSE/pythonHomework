ns = input().split()
nA = int(ns[0])
nB = int(ns[1])
kmS = input().split()
k = int(kmS[0])
m = int(kmS[1])

numsA = input().split()
for i in range(0, len(numsA)):
    numsA[i] = int(numsA[i])

numsB = input().split()
for i in range(0, len(numsB)):
    numsB[i] = int(numsB[i])

if numsA[k - 1] >= numsB[len(numsB) - m]:
    print('NO')
else:
    print('YES')