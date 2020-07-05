def ee(beginWord,endWord,wordList):
    import collections
    wordList.append(beginWord)
    buckets = collections.defaultdict(list)
    for word in wordList:
        for i in range(len(beginWord)):
            match = word[:i] + '_' + word[i + 1:]
            buckets[match].append(word)
    pres = collections.defaultdict(list)
    toSeen = collections.deque([(beginWord, 1)])
    befound = {beginWord: 1}
    while toSeen:
        cur, level = toSeen.popleft()
        for i in range(len(beginWord)):
            match = word[:i] + '_' + word[i + 1:]
            for word in buckets[match]:
                if word not in befound:
                    befound[word] = level + 1
                    toSeen.append((word, level + 1))
                if befound[word] == level + 1:
                    pres[word].append(cur)
        if endWord in befound and level + 1 > befound[endWord]:
            break
    if endWord in befound:
        res = [[endWord]]
        while res[0][0] != beginWord:
            res = [[word] + r for r in res for word in pres[r[0]]]
        print(res)
        return
    else:
        print([])
        return
if __name__ == '__main__':
    ee(input(),input(),eval(input()))
