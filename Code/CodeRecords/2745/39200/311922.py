def func():
    beginWord = input()
    endWord = input()
    wordList = [x[1:-1] for x in input()[1:-1].split(",")]
    if endWord not in wordList:
        return []
    else:
        wordict = set(wordList)
        s1 = {beginWord}
        s2 = {endWord}
        n = len(beginWord)
        step = 0
        wordict.remove(endWord)
        while s1 and s2:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return [w]
                    if w not in wordict: continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
    return []


print(func())