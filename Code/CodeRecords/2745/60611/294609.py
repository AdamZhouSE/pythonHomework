import sys
beginWord=input()
endWord=input()
wordList=list(eval(input()))
result=[]
if endWord not in wordList:
    print(0)
else:

    l = len(endWord)

    ws = set(wordList)

    head = {beginWord}
    tail = {endWord}
    tmp = list('abcdefghijklmnopqrstuvwxyz')
    res = 1
    while head:
        if len(head) > len(tail):
            head, tail = tail, head

        q = set()
        for cur in head:
            for i in range(l):
                for j in tmp:
                    word = cur[:i] + j + cur[i + 1:]

                    if word in tail:
                        result.append(res+1)
                        break

                    if word in ws:
                        q.add(word)
                        ws.remove(word)
        head = q
        res += 1
    print(min(result))