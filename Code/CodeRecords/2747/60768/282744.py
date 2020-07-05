class Solution:
    def find_ladders(self, begin, end, word):
        word = set(word)
        word.add(begin)
        if end not in word:
            return []
        # wordList.append(beginWord)
        dist = self.bfs(end, word)
        res = []
        self.dfs(begin, end, word, dist, [begin], res)
        return res

    # bfs记录点到终点的最短距离:end -> start ,广度优先确保最短
    def bfs(self, begin, word):
        dist = {begin: 0}
        queue = [begin]
        while queue:
            L = len(queue)
            for _ in range(L):
                word = queue.pop(0)
                for w in self.nextWord(word, word):
                    if w not in dist:
                        dist[w] = dist[word] + 1
                        queue.append(w)
        return dist

    # 利用递归来记录路径：从start -> end
    def dfs(self, curr, end, wordList, dist, path, res):
        if curr == end:
            res.append(list(path))
        for w in self.nextWord(curr, wordList):
            if dist[w] == dist[curr] - 1:  # 只有更逼近end的才行
                path.append(w)
                self.dfs(w, end, wordList, dist, path, res)
                path.pop()  # 深度优先，弹出，重新选接下去一个

    def nextWord(self, word, wordList):
        res = []
        for i in range(len(word)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                next_ = word[0:i] + letter + word[i + 1::]
                if next_ != word and next_ in wordList:
                    res.append(next_)
        return res


begin = input()
end = input()
word = eval(input())

print(Solution().find_ladders(begin, end, word))