questNum = int(input())

for quest in range(questNum):
    s = input()
    k = int(input())

    wordList = []
    diffWord = 1
    maxLen = 1
    for i in range(len(s) - 1):
        wordList.append(s[i])
        for j in range(i + 1, len(s)):
            if not s[j] in wordList:
                if diffWord == k:
                    temp = len(wordList)
                    if temp > maxLen:
                        maxLen = temp
                    wordList.clear()
                    wordList.append(s[i])
                    diffWord = 1
                else:
                    wordList.append(s[j])
                    diffWord += 1
            else:
                wordList.append(s[j])

    print(maxLen)