class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList=set(wordList)
        q=[(beginWord,1)]
        if endWord not in wordList:
            return []
        while q:
            node,level=q.pop(0)
            if node == endWord:
                return level
            for i in range(len(node)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new=node[:i]+j+node[i+1:]
                    if new in wordList:
                        q.append((new,level+1))
                        wordList.remove(new)
        return []
begin = input()
end = input()
words = eval(input())
s = Solution()
print(s.ladderLength(begin,end,words))