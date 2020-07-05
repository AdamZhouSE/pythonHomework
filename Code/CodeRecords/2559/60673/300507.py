def isIn(c, temp):
    for i in range(0, len(temp)):
        if c == temp[i]:
            return True
    return False


def removeRepeat(s):
    rmv = []
    for i in range(0, len(s)):
        if isIn(s[i], rmv):
            continue
        else:
            rmv.append(s[i])
    return rmv


def checkIsogram(s):
    rmv = removeRepeat(s)
    if len(rmv) == len(s):
        return True
    else:
        return False


t = int(input())
for i in range(0, t):
    inp = str(input())
    s = inp
    if checkIsogram(s):
        print(1)
    else:
        print(0)