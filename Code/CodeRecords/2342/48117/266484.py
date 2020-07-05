questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    s = input().split(' ')

    l = -k
    r = 0
    jump = False
    sStr = ''

    while r <= len(s):
        l += k
        r += k
        targetList = s[l:r]
        targetList = targetList[::-1]
        targetStr = ''
        for w in targetList:
            targetStr += w
        sStr += targetStr

    for i in range(len(sStr)):
        if i != len(sStr) - 1:
            print(sStr[i], end=' ')
        else:
            print(sStr[i])
