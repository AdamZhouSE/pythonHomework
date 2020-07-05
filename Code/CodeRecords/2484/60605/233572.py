
t = int(input())
liN = []
liM = []
liA = []
liB = []
for i in range(t):
    li = input().split(" ")
    liN.append(int(li[0]))
    liM.append(int(li[1]))
    liA.append(set(input().split(" ")))
    liB.append(set(input().split(" ")))

for i in range(t):
    setAB = liA[i].union(liB[i])
    print(len(setAB))