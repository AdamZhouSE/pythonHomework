def findLadders(beginWord: str, endWord: str, wordList):
    def buildPath(path,word):   
        if len(memories[word]) == 0:  
            res.append([word] + path)  
            return
        path.insert(0,word)  
        for element in memories[word]:
            buildPath(path,element)
        path.pop(0)
    memories = {} 
    memories[beginWord] = []
    wordList = set(wordList)
    wordList.discard(beginWord)
    for i in wordList:  
        memories[i] = []
    curset = set()
    curset.add(beginWord)
    preset = set()
    lenth = len(beginWord)
    res = []
    while True:
        preset = curset
        curset = set()
        for preword in preset:
            for i in range(lenth):
                left = preword[:i]
                right = preword[i+1:]
                for byte in "abcdefghijklmnopqrstuvwxyz":
                    if byte != preword[i]:
                        tempword = left + byte + right
                        if tempword in wordList:
                            memories[tempword].append(preword)
                            curset.add(tempword)
        for word in curset:
            wordList.discard(word)
        if len(curset) == 0:
            return []
        if endWord in curset:
            break
    buildPath([],endWord)
    return res


beginWord = input()
endWord = input()
dic = input()[1:-1].split(",")
dic = [x[1:-1] for x in dic]
res = findLadders(beginWord, endWord, dic)
if len(res) == 0:
    print(0)
else:
    print(len(res[0]))
