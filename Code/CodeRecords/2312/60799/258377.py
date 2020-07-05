n = int(input())
nList = [1] * (n + 1)
for i in range(2, n + 1):
    nList[i] = 0
    for j in range(0, i):
        nList[i] += nList[j] * nList[i - j - 1]
    nList[i] %= 1_000_000_007
print(nList[-1])
