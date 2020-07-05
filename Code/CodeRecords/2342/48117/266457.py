questNum = int(input())

for quest in range(questNum):
    nk = input().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    s = input().split(' ')
    sStr = ''
    for w in s:
        sStr += w

    l = -k
    r = 0
    jump = False
    while r <= len(sStr):
        l += k
        r += k
        targetStr = sStr[l:r]
        sStr = sStr[0:l] + targetStr[::-1] + sStr[r:]

    for i in range(len(sStr)):
        if i != len(sStr) - 1:
            print(sStr[i], end=' ')
        else:
            print(sStr[i])
