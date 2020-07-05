s = input()
nL = [int(i) for i in list(input())]
lim = int(input())
n = len(s)
mmm = set()
for i in range(n):
    total = 0
    for j in range(i, n, 1):
        if nL[j] == 0:
            total += 1
        if total>lim:
            break
        else:
            mmm.add(s[i:j+1])
print(len(mmm))
