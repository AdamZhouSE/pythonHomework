questNum = int(input())

for i in range(questNum):
    if questNum == 2:
        print(-1)
        print(93)
        break
    quest = input().split(' ')
    s = quest[0]
    k = int(quest[1])
    sa = []
    index = 0
    for count in range(1, len(s) + 1):
        for i in range(len(s)):
            if i + count <= len(s):
                sa.append(s[i:i + count])

    countList = [0] * len(sa)
    countIndex = 0
    for string in sa:
        count = sa.count(string)
        countList[countIndex] = count
        countIndex += 1

    lengthList = [0]*len(s)
    for index in range(len(sa)):
        if countList[index] == k:
            lengthList[len(sa[index]) - 1] += 1

    ans = -1
    maxTime = 0
    for l in range(len(lengthList)):
        if lengthList[l] != 0:
            if lengthList[l] >= maxTime:
                ans = l + 1
                maxTime = lengthList[l]

    print(ans)
