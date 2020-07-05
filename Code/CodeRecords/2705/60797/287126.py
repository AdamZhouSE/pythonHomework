class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        global fmap
        fmap = [0 for i in range(n + 1)] # 多加了一个fmap[0]
        candA = [0,0]
        candB = [0,0]

        # 查找有两个父节点的节点
        for edge in edges:
            if self.find(edge[1]) == 0:
                fmap[edge[1]] = edge[0]
            else:
                candA = [self.find(edge[1]), edge[1]]
                candB = [edge[0], edge[1]]
                edge[1] = 0

        # union-find查找环
        for i in range(n+1):
            fmap[i]=i
        for u, v in edges:
            if v == 0:
                continue
            if self.find(u) == self.find(v):
                if candA==[0,0]:
                    return edge
                return candA
            fmap[v] = u
        return candB

    def find(self, x):
        if fmap[x] == x:
            return x
        else:
            return self.find(fmap[x])

    '''
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            fmap[px] = py
    '''

if __name__ == '__main__':
    data = [[int(a) for a in item.strip('[]').split(',')] for item in input().split('], [')]
    s = Solution()
    data = [[5,2],[5,1],[3,1],[3,4],[3,5]]
    re = s.findRedundantDirectedConnection(data)
    print(re)
