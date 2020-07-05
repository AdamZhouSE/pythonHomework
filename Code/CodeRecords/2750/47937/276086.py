class Solution:

    # 贪心法

    def findMinHeightTrees(self, n, edges):

        if n <= 2:
            return [i for i in range(n)]

        from collections import defaultdict
        from collections import deque

        in_degrees = [0] * n
        # True 表示保留，如果设置为 False 则表示删除
        res = [True] * n
        # 邻接表
        adjs = defaultdict(list)
        for edge in edges:
            in_degrees[edge[0]] += 1
            in_degrees[edge[1]] += 1
            adjs[edge[0]].append(edge[1])
            adjs[edge[1]].append(edge[0])

        deque = deque()

        for i in range(n):
            if in_degrees[i] == 1:
                deque.append(i)

        # 根据示例，可知，最后可能剩下 1 个结点或者 2 个结点
        # 或者自己画一个图也能分析出来
        while n > 2:
            size = len(deque)
            # 一次减去当前队列这么多个结点
            n -= size
            for i in range(size):
                top = deque.popleft()
                res[top] = False

                successors = adjs[top]
                # 它和它的邻接点的入度全部减 1
                successors.append(top)

                for item in successors:
                    # 一个结点的入度重复减是没有关系的
                    # 我们只关心在最边界的那个结点，把它移除，所以可以认为是贪心法
                    in_degrees[item] -= 1

                    if in_degrees[item] == 1:
                        deque.append(item)

        return [i for i in range(len(res)) if res[i]]

a=int(input())
b=eval(input())
s=Solution()
print(s.findMinHeightTrees(a,b))