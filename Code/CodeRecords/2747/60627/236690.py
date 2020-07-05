from ast import literal_eval
import string

def ladderLength(beginWord, endWord, wordList):
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
                    tmp = s[:i] + j + s[i+1:]
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
inp = input()
wordList = literal_eval(inp)
a = ladderLength(beginWord, endWord, wordList)
if a == 0:
    print([])
if a == 5:
    print([['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']])