def findSuffix(s: str, suffix: list) -> list:
    for i in range(len(s)):
        suffix.append(s[i:])
    return suffix


qs = input().split(' ')
questNum = int(qs[0])
strLen = int(qs[1])
s = input()


for i in range(questNum):
    suffix1 = []
    suffix2 = []
    abcd = input().split(' ')
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])
    Sab = s[a - 1:b]
    Scd = s[c - 1:d]
    suffix1 = findSuffix(Sab, suffix1)
    suffix2 = findSuffix(Scd, suffix2)
    maxLen = 0
    
    for suffix in suffix1:
        if suffix in suffix2:
            if len(suffix) > maxLen:
                maxLen = len(suffix)

    print(maxLen)