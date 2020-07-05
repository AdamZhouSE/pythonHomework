def preOrder_print(aaa,l, r, f):
    if l == r:
        print(l, end=' ')
        return

    for i in range(l, 1 + r):
        if f[l][r] == f[l][i - 1] * f[i + 1][r] + aaa[i]:
            print(i, end=' ')
            preOrder_print(aaa,l, i - 1, f)
            preOrder_print(aaa,i + 1, r, f)
            return


dpList = [[0] * 32 for i in range(33)]
n = int(input())
aList = [int(i) for i in input().split()]
aList = [0]+aList+[0]*30
for i in range(2 + n):
    for j in range(2 + n):
        dpList[i][j] = 1
    dpList[i][i] = aList[i]

for i in range(n, 0, -1):
    for j in range(i + 1, n + 1):
        for k in range(i, j + 1, 1):
            dpList[i][j] = max(dpList[i][j], dpList[i][k - 1] * dpList[k + 1][j] + aList[k])

print(dpList[1][n])
preOrder_print(aList, 1, n, dpList)
