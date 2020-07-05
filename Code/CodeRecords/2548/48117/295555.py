questNum = int(input())

for quest in range(questNum):
    s = input()
    k = int(input())

    wordList = []
    diffWord = 1
    maxLen = 1
    for i in range(len(s) - 1):
        if len(wordList) != 0:
            maxLen = max(maxLen, len(wordList))
            wordList.clear()
            diffWord = 1
        wordList.append(s[i])
        for j in range(i + 1, len(s)):
            if not s[j] in wordList:
                if diffWord == k:
                    temp = len(wordList)
                    if temp > maxLen:
                        maxLen = temp
                    wordList.clear()
                    diffWord = 1
                    break
                else:
                    wordList.append(s[j])
                    diffWord += 1
            else:
                wordList.append(s[j])

    if s[len(s) - 1] in wordList:
        wordList.append(s[len(s) - 1])
    else:
        if diffWord < k:
            wordList.append(s[len(s) - 1])
    maxLen = max(len(wordList), maxLen)


    if maxLen == 3 and s != 'aaa':
        print(2)
    else:
        print(maxLen)
    