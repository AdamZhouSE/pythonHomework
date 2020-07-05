def getMin(n, lL, r):
    numberOne = n - (lL - 1)
    sum = numberOne
    for i in range(0, lL - 1):
        sum += 2 ** (i + 1)
    return sum


def getMax(n, lL, r):
    maxNum = 2 ** (r - 1)
    sum = 0
    for i in range(0, r - 1):
        sum += 2 ** i
    sum += maxNum * (n - (r - 1))
    return sum

nANDlANDr = input().split()
n = int(nANDlANDr[0])
lL = int(nANDlANDr[1])
r = int(nANDlANDr[2])

min = getMin(n, lL, r)
max = getMax(n, lL, r)
print(min, end=' ')
print(max)