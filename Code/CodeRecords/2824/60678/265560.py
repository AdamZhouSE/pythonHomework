nANDtANDc = input().split()
n = int(nANDtANDc[0])
t = int(nANDtANDc[1])
c = int(nANDtANDc[2])
imfo = input().split()
for i in range(0, n):
    imfo[i] = int(imfo[i])
count = 0
for i in range(0, n - c + 1):
    goodTogo = True
    for j in range(i, i + c):
        if imfo[j] > t:
            goodTogo = False
    if goodTogo:
        count += 1
print(count)