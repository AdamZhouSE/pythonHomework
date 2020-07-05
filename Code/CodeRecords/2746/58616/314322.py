# LeetCode 127
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0  
        l = len(endWord)
        ws = set(wordList)
        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head
            q = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i+1:]
                        if word in tail:
                            return res + 1
                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1
        return 0


begin = input()
end = input()
lst = eval(input())
s = Solution()
print(s.ladderLength(begin, end, lst))