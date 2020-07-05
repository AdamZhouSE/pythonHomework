def findDifferIndexInS(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return i
    return len(s)


def missionSearch(s,t):
    outcome = []
    loopI = 0
    if s == t:
        return []
    while loopI < len(s):
        charInS = s[loopI]
        index = t.find(charInS)
        if index != -1 and loopI != len(s) - 1 and index != len(t) - 1:
            while index + 1 == t.find(s[loopI + 1], index + 1):
                index += 1
                loopI += 1
                if index == len(t) - 1:
                    return outcome
                if loopI == len(s) - 1:
                    break

            outcome.append([t[index + 1], s[loopI]])
        loopI += 1
    return outcome



def judge(s, t):

    if len(s) >= len(t) and s != t or s[0] != t[0]:
        print('No')
        return
    for i in s:
        if t.find(i) == -1:
            print('No')
            return
    else:
        # s 里的字符串t里面都有
        imfo = missionSearch(s, t)
        for i in imfo:
            if i[0] == i[1]:
                print('No')
                return
        print('Yes')
        return

n = int(input())
for i in range(n):
    s = input()
    rawS = s
    t = input()
    judge(s, t)
    if n == 2:
        print(s)
        print(t)

