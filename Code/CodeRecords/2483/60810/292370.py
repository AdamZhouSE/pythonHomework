'''
给定一个字符串str和另一个字符串patt。在str中的最小索引处找到patt中的字符。如果str中不存在patt字符，则打印$
'''


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