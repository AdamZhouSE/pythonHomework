from collections import deque, namedtuple

TreeNode = namedtuple('TreeNode', ['row', 'col', 'id'])


class Solution:
    def cutOffTree(self, forest):
        M = len(forest)
        N = len(forest[0])
        tree_lst = []
        for i in range(M):
            for j in range(N):
                c = forest[i][j]
                if c > 1:
                    tree_lst.append(c)
        tree_lst = sorted(tree_lst)
        nt = len(tree_lst)

        length_step = 0

        visited = [[-2 for i in range(N)] for j in range(M)]

        q = deque()

        if tree_lst[0] == forest[0][0]:
            q.append(TreeNode(0, 0, 0))
            visited[0][0] = 0
        else:
            q.append(TreeNode(0, 0, -1))

        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while q:
            nq = len(q)
            while nq:
                nq = nq - 1
                node = q.popleft()

                if node.id == nt - 1:
                    return length_step
                for d in dirs:
                    row = node.row + d[0]
                    col = node.col + d[1]
                    cur_id = node.id

                    if row < 0 or row >= M or col < 0 or col >= N:
                        continue
                    c = forest[row][col]

                    if c == 0:
                        continue

                    if c > 1 and tree_lst.index(c) == node.id + 1:
                        cur_id = node.id + 1

                    if visited[row][col] >= cur_id:
                        continue
                    visited[row][col] = cur_id
                    q.append(TreeNode(row, col, cur_id))

            length_step = length_step + 1
        return -1

import sys
lines = []
for line in sys.stdin:
    lines.append(line)
temp2 = []
for i in range(1,len(lines)-1):
    temp1 = []
    for item in lines[i]:
        if item.isdigit():
            temp1.append(item)
    temp2.append(temp1)
for i in range(len(temp2)):
    for j in range(len(temp2[i])):
        temp2[i][j] = int(temp2[i][j])
print(Solution().cutOffTree(temp2))