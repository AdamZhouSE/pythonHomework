# DFS 深度优先搜索


def ladderLength(beginWord, endWord, wordDict):
    from collections import defaultdict
    visited = []   # 记录已遍历的单词
    neighbors = defaultdict(list)
    wordDict.append(beginWord)

    def getNeighbors(aWord):
        ans = []
        for word in wordDict:
            if aWord != word and wordDiff(aWord, word) == 1:
                ans.append(word)
        return ans

    for word in wordDict:
        neighbors[word] = getNeighbors(word)
        
    if endWord not in wordDict:
        return []

    res = []
    flag = False
    loops = 0
    tmp = [beginWord]
    stack = [beginWord]
    while len(visited) != len(wordDict)-2:
        while stack:  # DFS
            if flag:
                flag = False
                break

            cur = stack.pop()
            for neighbor in getNeighbors(cur):
                if wordDiff(neighbor, endWord) == 1:
                    tmp.append(neighbor)
                    visited.append(neighbor)
                    tmp.append(endWord)
                    flag = True
                    res.append(tmp)
                    break

                if neighbor not in visited:
                    stack.append(cur)
                    stack.append(neighbor)
                    visited.append(neighbor)
                    tmp.append(neighbor)
                    break

        tmp = [beginWord]
        stack.append(beginWord)
        for c in getNeighbors(beginWord):
            if c in visited:
                visited.remove(c)
        loops += 1
        if loops > 50:
            return []
    return res


def wordDiff(wordA, wordB):
    count = 0
    for i in range(len(wordB)):
        if wordA[i] != wordB[i]:
            count += 1
    return count


beginWord = input()
endWord = input()
wordList = eval(input())
print(ladderLength(beginWord, endWord, wordList))
