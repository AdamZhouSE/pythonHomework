from collections import deque, namedtuple
TreeNode = namedtuple('TreeNode', ['row', 'col', 'id'])
s, temp_s = "", ""
while temp_s != ']':
    temp_s = input()
    s += temp_s
forest = eval(s)

def sol():
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
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    while q:
        nq = len(q)
        while nq:
            nq = nq - 1
            node = q.popleft()
            # 判断是否已经砍了所有树
            if node.id == nt - 1:
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
                if visited[row][col] >= cur_id:
                    continue
                visited[row][col] = cur_id
                q.append(TreeNode(row, col, cur_id))
        # 下一层
        length_step = length_step + 1
    return -1

print(sol())