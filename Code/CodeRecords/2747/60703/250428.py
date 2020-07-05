class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        wordList.add(beginWord)
        if(endWord not in wordList):
            return []
        # wordList.append(beginWord)
        dist = self.bfs(endWord, wordList)
        res = []
        self.dfs(beginWord, endWord, wordList, dist, [beginWord], res)
        return res

    # bfs记录点到终点的最短距离:end -> start ,广度优先确保最短
    def bfs(self, begin, wordList):
        dist = {}
        dist[begin] = 0
        queue = [begin]
        while queue:
            L = len(queue)
            for _ in range(L):
                word = queue.pop(0)
                for w in self.nextWord(word, wordList):
                    if w not in dist:
                        dist[w] = dist[word] + 1
                        queue.append(w)
        return dist

    # 利用递归来记录路径：从start -> end
    def dfs(self, curr, end, wordList, dist, path, res):
        if curr == end:
            res.append(list(path))
        for w in self.nextWord(curr, wordList):
            if dist[w] == dist[curr] - 1:#只有更逼近endword的才行
                path.append(w)
                self.dfs(w, end, wordList, dist, path, res)
                path.pop()#深度优先，弹出，重新选接下去一个

    def nextWord(self, word, wordList):
        res = []
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                next_ = word[0:i] + letter + word[i + 1::]
                if next_ != word and next_ in wordList:
                    res.append(next_)
        return res




beginWord = input();
endWord = input();
wordList = eval(input());

print(Solution().findLadders(beginWord,endWord,wordList));


beginWord = input();
endWord = input();
wordList = eval(input());

print(Solution().findLadders(beginWord,endWord,wordList));








