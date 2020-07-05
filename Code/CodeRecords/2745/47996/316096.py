def findLadders(beginWord, endWord, wordlist):
    ans,q = {},[]
    q.append(beginWord)
    ans[beginWord] = [[beginWord]]
    ans[endWord] = []
    while len(q) != 0:
        tmp = q.pop(0)
        for i in range(len(beginWord)):
            part1,part2 = tmp[:i],tmp[i + 1:]
            for j in "abcdefghijklmnopqrstuvwxyz":
                if tmp[i] != j:
                    newword = part1 + j + part2
                    if newword == endWord:
                        for k in ans[tmp]:
                            ans[endWord].append(k + [endWord])
                        while len(q) != 0:
                            tmp1 = q.pop(0)
                            if len(ans[tmp1][0]) >= len(ans[endWord][0]):
                                break
                            for ni in range(len(beginWord)):
                                npart1,npart2 = tmp1[:ni],tmp1[ni+1:]
                                for nj in "abcdefghijklmnopqrstuvwxyz":
                                    if tmp1[ni] != nj:
                                        nw = npart1 + nj + npart2
                                        if endWord == nw:
                                            for nk in ans[tmp1]:
                                                ans[endWord].append(nk + [endWord])
                        break
                    if newword in wordlist:
                        q.append(newword)
                        ans[newword] = []
                        for k in ans[tmp]:
                            ans[newword].append(k + [newword])
                        wordlist.remove(newword)
                    elif newword in ans and len(ans[newword][0]) == len(ans[tmp][0]) + 1:
                        for k in ans[tmp]:
                            ans[newword].append(k + [newword])
    return ans[endWord]
beginWord = input()
endWord = input()
dic = input()[1:-1].split(",")
res = findLadders(beginWord, endWord, dic)
print(res)
