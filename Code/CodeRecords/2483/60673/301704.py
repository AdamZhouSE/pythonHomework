def isIn(c, s):
    for i in range(0, len(s)):
        if c == s[i]:
            return True
    return False


def findChar(s, patt):
    for i in range(0, len(s)):
        if isIn(s[i], patt):
            return s[i]
    return '$'


n = int(input())
for i in range(0, n):
    s = str(input())
    patt = str(input())
    res = findChar(s, patt)
    print(res)