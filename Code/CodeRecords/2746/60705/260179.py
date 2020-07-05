import collections


def ladderLength(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 1

    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    word_graph = collections.defaultdict(list)
    word_len = len(beginWord)
    wordList.append(beginWord)
    for word in wordList:
        for i in range(word_len):
            wildcast = word[:i] + '*' + word[i + 1:]
            word_graph[wildcast].append(word)

    res = 1
    left_q, right_q = {beginWord}, {endWord}
    wordSet.discard(beginWord)
    wordSet.discard(endWord)
    while left_q:
        nxt_q = set()
        for cur in left_q:
            for i in range(word_len):
                wildcast = cur[:i] + '*' + cur[i + 1:]
                for nxt in word_graph[wildcast]:
                    if nxt in right_q:
                        return res + 1
                    if nxt in wordSet:
                        nxt_q.add(nxt)
                        wordSet.discard(nxt)
        res += 1
        left_q = nxt_q
        if len(left_q) > len(right_q):
            left_q, right_q = right_q, left_q
    return 0


if __name__ == '__main__':
    beginWord = input()
    endWord = input()
    wordList = input()[1:-1].split(",")
    for i in range(0, len(wordList)):
        wordList[i] = wordList[i][1:-1]
    print(ladderLength(beginWord, endWord, wordList))
