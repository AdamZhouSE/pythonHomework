from typing import List
from collections import deque, namedtuple

TreeNode = namedtuple('TreeNode', ['row','col','id'])
class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        # 采用广度优先搜索,首先把树取出来,然后再排序，然后从起点开始搜索，记录已经修剪到的树
        # 状态：当前修剪的树的编号。下一次修剪的树的编号是在此基础上加1
        # 若当前此状态曾经访问过，则跳过此状态。需要用一个数组存放状态，数组的大小与forest大小相同

        # 读取树，并排序
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
        # 当前已经走的边长度
        length_step = 0

        # 保存状态
        visited = [[-2 for i in range(N)] for j in range(M)]
        # 初始化的队列
        q = deque()

        if tree_lst[0] == forest[0][0]:
            q.append(TreeNode(0, 0, 0))
            visited[0][0] = 0
        else:
            q.append(TreeNode(0, 0, -1))

        # 遍历的方向
        dirs = [(0, -1),(0, 1),(1, 0), (-1, 0)]

        while q:
            nq = len(q)
            while nq:
                nq = nq -1
                node = q.popleft()
                # 判断是否已经砍了所有树
                if node.id == nt -1:
                    return length_step
                for d in dirs:
                    row = node.row + d[0]
                    col = node.col + d[1]
                    cur_id = node.id
                    # 是否越界
                    if row < 0 or row >= M or col < 0 or col >= N:
                        continue
                    c = forest[row][col]
                    # 是否是墙
                    if c == 0:
                        continue
                    # 是否是树且是接下来要砍的树
                    if c > 1 and tree_lst.index(c) == node.id + 1:
                        # 记录当前砍到了第几个树
                        cur_id = node.id + 1
                    # 判断当前状态是否曾经到达过，若到达过，则此前到达的时候肯定比此次到达更优，则跳过；否则加入队列
                    if visited[row][col]>= cur_id:
                        continue
                    visited[row][col] = cur_id
                    q.append(TreeNode(row, col, cur_id))
            # 下一层
            length_step = length_step + 1
        return -1

biglist=""
try:
    while True:
        s = input()
        biglist=biglist+s
except EOFError:
    pass

#print(biglist)
str(biglist)
biglist=biglist.replace(' ','')
biglist=eval(biglist)
#print(biglist)
#print(biglist[0])
#print(biglist[0][0])

s=Solution()
print(s.cutOffTree(biglist))