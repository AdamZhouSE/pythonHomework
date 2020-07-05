def find(beginWord, endWord, wordList):
        beginList, wordSet, res = [[beginWord]], set(wordList), []
        if endWord not in wordList:
            return res
        while beginList:
            for one in beginList:
                if one[-1] in wordSet:
                    wordSet.remove(one[-1])
            for _ in range(len(beginList)):
                one = beginList.pop(0)
                word = one[-1]
                for i in range(len(word)):
                    tmp = list(word)
                    for c in list(map(chr, range(ord('a'), ord('z')+1))):
                        tmp[i] = c
                        str_tmp = ''.join(tmp)
                        if str_tmp == endWord:
                            res.append(one+[str_tmp])
                        elif str_tmp in wordSet:
                            beginList.append(one+[str_tmp])
            if res:
                return res
        return res
beginword=input()
endword=input()
wordlist=input()
answer=find(beginword,endword,wordlist)
print(answer)