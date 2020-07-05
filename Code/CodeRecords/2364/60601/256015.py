import math

def numDupDigitsAtMostN(N: int):
    s = str(N)
    n = len(s)
    nodup = 0
    for i in range(1, n + 1):
        nodup += 9 * math.factorial(9) / math.factorial(9 - i + 1)
    dup = {}
    for i in range(n):
        a = int(s[i])
        for m in range(a + 1, 10):
            if m not in dup:
                nodup -= math.factorial(9 - len(dup)) / math.factorial(9 - len(dup) - n + 1 + i)
        if a in dup:
            break
        dup[a] = 1
    return int(N - nodup)
print(numDupDigitsAtMostN(eval(input())))