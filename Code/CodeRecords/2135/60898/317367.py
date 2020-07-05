import math
def strtoInt(s: str)-> int:
    return int(s)

def leastStep(l: list) -> int:

    MIN_MID = 0
    MIN_POW = 1000000000
    t = sorted(l)
    small = t[0]
    large = t[-1]
    total = 0.0
    delta = 0
    for i in range(small, large + 1):
        for j in l :
            total += (j - i) * (j - i)
        if total < MIN_POW :
            MIN_MID = i
            MIN_POW = total
        total = 0

    for i in l :
        delta += abs(i - MIN_MID)
    return delta

l = list(map(strtoInt, input().strip().split(",")))
print(leastStep(l))