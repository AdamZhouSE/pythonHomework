import collections
import re


def bfs(forest, sr, sc, tr, tc):
    R, C = len(forest), len(forest[0])
    queue = collections.deque([(sr, sc, 0)])  # 创建一个队列，进行BFS
    seen = {(sr, sc)}  # 记录路线
    while queue:
        r, c, d = queue.popleft()  # 出队列
        if r == tr and c == tc:
            return d
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):  # 上下左右
            if (0 <= nr < R and 0 <= nc < C and
                    (nr, nc) not in seen and forest[nr][nc]):  # 没有在记录的路线中并且不为0
                seen.add((nr, nc))
                queue.append((nr, nc, d + 1))
    return -1


matrix = []
maxNum = 0
x = 0
y = 0
while True:
    temp = input()
    if temp == '[':
        continue
    if temp == ']':
        break
    else:
        line = [int(i) for i in re.findall("\d+", temp)]
        if maxNum < max(line):  # 更新最大的数及其坐标
            maxNum = max(line)
            x = len(matrix)
            y = line.index(maxNum)
        matrix.append(line)
print(bfs(matrix, 0, 0, x, y))
