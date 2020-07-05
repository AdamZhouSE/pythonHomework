hmb = input().split()
M = int(hmb[0])
M = max(M, 1)
N = int(hmb[1])
res = [0]*10
for i in range(M, N+1):
    aList = [int(j) for j in list(str(i))]
    aSet = set(aList)
    for j in aSet:
        res[j] += aList.count(j)
print(' '.join([str(i) for i in res]), end='')