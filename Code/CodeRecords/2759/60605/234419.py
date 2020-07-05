t = int(input())
liM = []
liN = []
liA = []
liB = []
for i in range(t):
    a = input().split(" ")
    liM.append(int(a[0]))
    liN.append(int(a[1]))
    liA.append(int(a[2]))
    liB.append(int(a[3]))

for i in range(t):
    m = liM[i]
    n = liN[i]
    a = liA[i]
    b = liB[i]
    cnt = 0
    for j in range(m, n + 1):
        if j % a == 0 or j % b == 0:
            cnt += 1
    print(cnt)
