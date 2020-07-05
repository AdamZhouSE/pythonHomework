def f(s, i):
    charList = []
    for var in s:
        if var not in charList:
            charList.append(var)
    if len(charList) == i:
        return True
    else:
        return False


size = int(input())
for i in range(size):
    s = input()
    charList = []
    for var in s:
        if var not in charList:
            charList.append(var)
    leastLength = len(charList)
    start = 0
    resultList = []
    while start < len(s):
        j = leastLength
        while start + j - 1 < len(s):
            t = s[start:start + j]
            if f(t, len(charList)):
                resultList.append(j)
            j += 1
        start += 1
    lw = sorted(resultList)
    print(lw[0])
