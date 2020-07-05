class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        res = 1
        q = [beginWord]
        while len(q)!=0:
            k = len(q)
            for n in range(k):
                word = q.pop(0)
                if word==endWord:
                    return res
                for i in range(len(word)):
                    newWord = word
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet and newWord!=word:
                            q.append(newWord)
                            wordSet.remove(newWord)
            res += 1
        return 0
————————————————
版权声明：本文为CSDN博主「哪得小师弟」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/x603560617/article/details/87992660