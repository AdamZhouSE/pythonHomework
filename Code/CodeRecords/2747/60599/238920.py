def g(beginWord, endWord, z, q):
    for i in q:
        q[i] = list(q[i])
    e = []
    for w in z:
        l = f(q, w)  # 将结果相连成小段
        l1 = []
        l2 = []
        for i in l:
            if (i[-1] == beginWord):
                l1.append(i)
            elif (i[-1] == endWord):
                l2.append(i)
            if (i[0] == endWord and i[-1] == beginWord):
                e.append(i[::-1])  # 长度为2
            elif (i[0] == beginWord and i[-1] == endWord):
                e.append(i)
        for a in l1:
            for b in l2: e.append(a[::-1] + b[1:])  # 前后小段相连成完整段
    return e


def f(q, word):
    if (q[word][0] == word): return [[word]]  # 到了beginWord 或是 endWord
    e = []
    for i in q[word]:
        for w in f(q, i):
            e.append([word] + w)
    return e

def findLadders(beginWord, endWord, wordList):
    q = {beginWord: {beginWord}}
    z = set()  # 统计相遇节点
    wl = len(beginWord)
    begin_set, end_set = {beginWord}, {endWord}
    wordList = set(wordList)
    if endWord not in wordList: return []
    i = 1
    while begin_set and end_set:
        i = i + 1
        if len(begin_set) > len(end_set): begin_set, end_set = end_set, begin_set
        nextList = set()
        u = 0
        for word in begin_set:
            for j in range(wl):
                for k in range(26):
                    nextWord = word[:j] + chr(k + 97) + word[j + 1:]
                    if nextWord in end_set:
                        z.add(nextWord)
                        if (nextWord in q):
                            q[nextWord].add(word)
                        else:
                            q[nextWord] = {word}
                    elif nextWord in wordList:
                        if (nextWord in q):
                            q[nextWord].add(word)
                        else:
                            q[nextWord] = {word}
                        if (nextWord not in nextList): nextList.add(nextWord)
        for www in nextList: wordList.remove(www)
        if z != set():
            k=g(beginWord, endWord, z, q)
            k.sort()
            print(k) # 因为要求的是最短路径，有结果直接返回就是了
            exit()
        begin_set = nextList
a=input()
b=input()
s=list(eval(input()))
findLadders(a,b,s)
print([])