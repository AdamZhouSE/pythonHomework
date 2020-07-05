import string
def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    wordDict, step = set(wordList), 1
    if endWord not in wordDict:
        return 0

    s1, s2 = set([beginWord]), set([endWord])
    while s1:
        stack = set([])
        wordDict -= s1

        for s in s1:
            for i in range(len(beginWord)):
                for j in string.ascii_lowercase:
                    tmp = s[:i] + j + s[i + 1:]
                    if tmp not in wordDict:
                        continue
                    if tmp in s2:
                        return step + 1
                    stack.add(tmp)

        if len(stack) < len(s2):
            s1 = stack
        else:
            s1, s2 = s2, stack
        step += 1
    return 0

beginWord = input()
endWord = input()
wordList = input()[1:-1].split(",")
i=0
while i<len(wordList):
    wordList[i]=wordList[i][1:-1]
    i+=1
print(ladderLength(beginWord, endWord, wordList))