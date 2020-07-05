import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordlist = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword = w[:i] + c + w[i + 1:]
                            if newword in wordlist:
                                newlayer[newword] += [j + [newword] for j in layer[w]]
            wordlist -= set(newlayer.keys())
            layer = newlayer

        return res


input1 = input()
input2 = input()
inputStr = input()
strs = inputStr.replace("[", "").replace("]", "").replace('"', '').split(",")
print(Solution().findLadders(input1, input2, strs))print(Solution().findLadders(input1, input2, strs))