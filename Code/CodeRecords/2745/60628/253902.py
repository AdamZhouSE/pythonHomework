def findLadders(beginWord, endWord, wordList):
    beginList, wordset, res = [[beginWord]], set(wordList), []
    while beginList:
        for newWordList in beginList:
            if newWordList[-1] in wordset:
                wordset.remove(newWordList[-1])
        for _ in range(len(beginList)):
            newWordList = beginList.pop(0)
            word = newWordList[-1]
            for i in range(len(word)):
                for c in list(map(chr, range(ord('a'), ord('z') + 1))):
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord == endWord:
                        res.append(newWordList + [newWord])
                    elif newWord in wordset:
                        beginList.append(newWordList + [newWord])
        return res
    return res

beginWord = input()
endWord = input()
wordList = eval(input())
print(findLadders(beginWord, endWord, wordList))
