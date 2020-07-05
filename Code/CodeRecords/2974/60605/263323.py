def isPositiveCycle(s: str) -> bool:
    if len(s) % 2 == 0: return False
    ss = list(s)
    cc = ss.copy()
    cc.reverse()
    return ss == cc

def howManyGoodSubstrs(s: str) -> int:
    sets = set()
    leng = len(s)
    cnt = 0
    for i in range(0, leng):
        for j in range(i, leng):
            if isPositiveCycle(s[i:j+1]):
                sets.add(s[i:j+1])
    return len(sets)

def howManyAntiGoodSubstrs(s: str) -> int:
    sets = set()
    leng = len(s)
    cnt = 0
    for i in range(0, leng):
        for j in range(i, leng):
            if not isPositiveCycle(s[i:j+1]):
                sets.add(s[i:j+1])
    return len(sets)

if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    maxScore = 0
    for i in range(1, n):
        # a: 0-(i-1)
        # b: i-
        s1 = s[0:i]
        s2 = s[i:]
        c1 = howManyGoodSubstrs(s1)
        c2 = howManyAntiGoodSubstrs(s2)
        maxScore = max(maxScore, c1*c2)

    print(maxScore)