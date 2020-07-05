from _collections import defaultdict
begin, end = input(), input()
words = set(eval(input()))

def solution():
    if end not in words or not words or not words:
        return 0
    combo_dict = defaultdict(list)
    # 构造邻接表
    for word in words:
        for i in range(len(begin)):
            combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
    queue = [(begin, 1)]
    visited = {begin: True}
    while queue:
        current, level = queue.pop(0)
        for i in range(len(begin)):
            inter = current[:i] + '*' + current[i + 1:]
            for word in combo_dict[inter]:
                if word == end:
                    return level + 1
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            combo_dict[inter] = []
    return 0

print(solution())