def isIn(c, rmv):
    for i in range(0, len(rmv)):
        if c == rmv[i]:
            return True
    return False


def isVowel(c):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if isIn(c, vowel):
        return True
    return False


def difStr(s):
    rmv = []
    for i in range(0, len(s)):
        if isVowel(s[i]):
            continue
        if isIn(s[i], rmv):
            continue
        else:
            rmv.append(s[i])
    length = len(rmv)
    if length % 2 == 0:
        print('SHE!')
    else:
        print('HE!')


n = int(input())
for i in range(0, n):
    s = str(input())
    difStr(s)