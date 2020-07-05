# BFS
beginWord = input()
endWord = input()
wordList = set(eval(input()))
res = []
if endWord not in wordList:
    pass
else:
    q = [beginWord]#BFS同一层的节点
    visited = set()#visited保存经访问确定无法到达endWord的节点，也即所有访问过的节点中除去构成正确通路的节点
    trace = []
    while q:
        word = q.pop(0)
        if word in visited:#从该单词往下查找无法到达endWord，趁早放弃
            pass
        else:
            visited.add(word)
            trace.append(word)
            if word==endWord:
                res.append(trace)
                for w in trace:
                    visited.remove(w)
                trace = []
                q = [beginWord]
            else:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = word[:i]+j+word[i+1:]
                        if (tmp not in visited) and (tmp in wordList):
                            q.append(tmp)
print(res)