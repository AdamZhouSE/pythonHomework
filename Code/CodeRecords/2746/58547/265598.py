# BFS 广度优先遍历
def min_conversion_len(primary, target, vocabulary):
    from collections import deque
    vocabulary = set(vocabulary)
    if target not in vocabulary:
        return 0
    visited = set()

    # 看两个单词是否差一个字母
    def is_one_letter(w, word):
        if len(w) != len(word):
            return False
        dif = 0
        for i in range(len(w)):
            if w[i] != word[i]: dif += 1
            if dif > 1: return False
        return True

    # 发现所有和word相差一个字母的单词
    def find_only_one_letter(word):
        ans = []
        for w in vocabulary:
            # print(is_one_letter(w, word))
            if w not in visited and is_one_letter(w, word):
                ans.append(w)
        # print(ans)
        return ans

    queue = deque()
    queue.appendleft(primary)
    res = 1
    # BFS
    while queue:
        n = len(queue)
        for _ in range(n):
            tmp = queue.pop()
            if tmp == target:
                return res
            visited.add(tmp)
            for t in find_only_one_letter(tmp):
                queue.appendleft(t)
        res += 1
    return 0


def func():
    primary = input()
    target = input()
    vocabulary = input()[2:-2].split("\",\"")
    print(min_conversion_len(primary, target, vocabulary))


func()
