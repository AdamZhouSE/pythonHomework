from collections import defaultdict

used = []
beginWord = input()
endWord = input()
wordList = eval(input())
ans = []
parents1 = {beginWord: -1}
parents2 = {endWord: -1}
wordDic = defaultdict(list)
if endWord not in wordList:
    print(ans)
    exit(0)
else:
    for word in wordList:
        for i in range(len(word)):
            interWord = word[:i] + '*' + word[i + 1:]
            wordDic[interWord].append(word)


def bfs(queue, parents, selfVisited, otherVisited):
    curWord, count = queue.pop()
    for j in range(len(curWord)):
        nextPattern = curWord[:j] + '*' + curWord[j + 1:]
        for word in wordDic[nextPattern]:
            if word in otherVisited:
                parents.update({word: curWord})
                return [count + otherVisited[word], word]
            if word not in selfVisited:
                selfVisited.update({word: count + 1})
                queue.append((word, count + 1))
                parents.update({word: curWord})
    return None


queue1 = []
queue2 = []
queue1.append((beginWord, 1))
queue2.append((endWord, 1))

dic1 = {}
dic2 = {}
dic1.update({beginWord: 1})
dic2.update({endWord: 1})
answers = []
while queue1 and queue2:
    res = bfs(queue1, parents1, dic1, dic2)
    if res:
        wor = res[1]
        used.append(wor)
        ans = [wor]
        p1 = wor
        while parents1[p1] != -1:
            ans.append(parents1[p1])
            p1 = parents1[p1]
        ans.reverse()
        p2 = wor
        while parents2[p2] != -1:
            ans.append(parents2[p2])
            p2 = parents2[p2]
        if ans not in answers:
            answers.append(ans)
    res = bfs(queue2, parents2, dic2, dic1)
    if res:
        wor = res[1]
        used.append(wor)
        ans = [wor]
        p1 = wor
        while parents1[p1] != -1:
            ans.append(parents1[p1])
            p1 = parents1[p1]
        ans.reverse()
        p2 = wor
        while parents2[p2] != -1:
            ans.append(parents2[p2])
            p2 = parents2[p2]
        if ans not in answers:
            answers.append(ans)
answers.sort()
print(answers)