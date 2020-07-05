def toInt(c):
    if c == 'I': return 1
    if c == 'V': return 5
    if c == 'X': return 10
    if c == 'L': return 50
    if c == 'C': return 100
    if c == 'D': return 500
    if c == 'M': return 1000


nstr = input()
n = len(nstr)
res = 0
for i in range(0, n - 1):
    cur = toInt(nstr[i])
    nextc = toInt(nstr[i + 1])
    if ((cur == 1) & ((nextc == 5) | (nextc == 10))) | ((cur == 10) & ((nextc == 50) | (nextc == 100))) | (
            (cur == 100) & ((nextc == 500) | (nextc == 1000))):
        res -= cur
    else:
        res += cur
res += nextc
print(res)