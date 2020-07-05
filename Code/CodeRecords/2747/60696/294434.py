res = []


def can_transfer(word1, word2):
    cnt = 0
    for i in range(n):
        if word1[i] != word2[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def find_path(path:list, index):
    if can_transfer(path[-1], beginWord):
        path.append(beginWord)
        path.reverse()
        min_step = len(wordDict)+2
        for j in range(len(res)):
            min_step = min(min_step, len(res[j]))
        if len(path) < min_step:
            res.clear()
            res.append(path)
        elif len(path) == min_step:
            res.append(path)
        else:
            pass
        return
    if index < 0:
        return
    for i in range(index, -1, -1):
        if can_transfer(path[-1], wordDict[i]):
            temp = path.copy()
            temp.append(wordDict[i])
            find_path(temp, index-1)
    return


if __name__ == '__main__':
    beginWord = input()
    endWord = input()
    n = len(beginWord)
    wordDict = list(eval(input()))
    if endWord in wordDict:
        wordDict.remove(endWord)
        find_path([endWord], len(wordDict)-1)
        if len(res)==0:
            print(res)
        else:
            print('[')
            for i in range(len(res)-1):
                print(res[i], end=',\n')
            print(res[-1])
            print(']')
    else:
        print(res)
