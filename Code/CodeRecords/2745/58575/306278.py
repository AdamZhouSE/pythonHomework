import string
from collections import defaultdict
def findLadders(beginWord, endWord, wordList):
    wordDict, res = set(wordList), []
    if endWord not in wordDict:
        return res

    s1, s2, step = defaultdict(list), defaultdict(list), 2
    s1[beginWord].append([beginWord])
    s2[endWord].append([endWord])
    while s1:
        stack = defaultdict(list)
        wordDict -= s1.keys()

        for w, paths in s1.items():
            for i in range(len(w)):
                for j in string.ascii_lowercase:
                    tmp = w[:i] + j + w[i + 1:]
                    if tmp not in wordDict:
                        continue
                    if tmp in s2:
                        if paths[0][0] == beginWord:
                            res += [f + b[::-1] for f in paths for b in s2[tmp]]
                        else:
                            res += [b + f[::-1] for f in paths for b in s2[tmp]]
                    stack[tmp] += [p + [tmp] for p in paths]

        if len(stack) < len(s2):
            s1 = stack
        else:
            s1, s2 = s2, stack
        step += 1
        if res and step > len(res[0]):
            return res
    return res

beginword=input()
endword=input()
wordlist=input()[1:-1].split(",")
i=0
while i<len(wordlist):
    wordlist[i]=wordlist[i][1:-1]
    i+=1

res=findLadders(beginword,endword,wordlist)
print(res)