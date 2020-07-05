class DSU:
    def __init__(self, R, C):
        #R * C is the source, and isn't a grid square
        self.par = list(range(R*C + 1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8],并查集初始化各自为各自的集合
        self.rnk = [0] * (R*C + 1) # 相当于合并次数
        self.sz = [1] * (R*C + 1) # 表示集合中节点的数目，由于初始化每个节点都在自己的集合，所以都是1

    def find(self, x):
        if self.par[x] != x: # find终止条件就是一直向上find，直到parent[x]=x，自己就是代表节点
            self.par[x] = self.find(self.par[x]) # 递归查找
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.sz[xr] += self.sz[yr] # 集合节点数量合并

    def size(self, x):
        return self.sz[self.find(x)] # 表示集合中节点的数目

    def top(self): # 求顶部那个集合的大小
        # Size of component at ephemeral "source" node at index R*C,
        # minus 1 to not count the source itself in the size
        return self.size(len(self.sz) - 1) - 1 # len(self.sz) - 1其实就是R*C

class Solution(object):
    def hitBricks(self, grid, hits):
        R, C = len(grid), len(grid[0])

        def index(r, c): # 将坐标(x,y)转化为index
            return r * C + c

        def neighbors(r, c): # 迭代生成符合题意的邻居节点
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid] # [[1, 0, 0, 0], [1, 1, 1, 0]]，其实就是grid，相当于深拷贝了
        for i, j in hits: # 先去掉hits里面所有位置的砖头
            A[i][j] = 0

        dsu = DSU(R, C) # 下面开始构造不考虑hits情况下的并查集
        for r, row in enumerate(A):
            for c, val in enumerate(row): # (r,c)相当于位置，val为当前位置的值
                if val: # 该位置有砖头
                    i = index(r, c) # 坐标转换为index，因为使用list实现的并查集
                    if r == 0: # 是第一行顶部
                        dsu.union(i, R*C) # 合并到R*C一派，R*C是标记的顶部集合,我们定义的，因为最大index是R*C-1，设成别的也ok
                    if r and A[r-1][c]: # 不是第一行并且上一行有砖头
                        dsu.union(i, index(r-1, c)) # 合并到上一行那一派
                    if c and A[r][c-1]: # 不是最左边并且左边有砖头
                        dsu.union(i, index(r, c-1)) # 合并到最左边
        # print(dsu.par) # [0, 1, 2, 3, 4, 6, 6, 7, 0] # 这样看并查集内容，你可以放在上面循环里面打印

        ans = []
        for r, c in reversed(hits): # 反向思考，如果我们是往上放砖,
            # 为什么要反向？因为如果是拿砖，后一次会影响前一次，放砖就是前一次被后一次影响
            pre_roof = dsu.top() # 保存并查集现在的状态
            if grid[r][c] == 0: # 此处无砖，结果不变
                ans.append(0)
            else:
                i = index(r, c) # 若此处有砖，求坐标
                for nr, nc in neighbors(r, c): # 遍历四周连接砖头
                    if A[nr][nc]: # 如果有砖
                        dsu.union(i, index(nr, nc)) #归到一类
                if r == 0:
                    dsu.union(i, R*C) # 如果是顶部，归到顶部自定义的R*C类
                A[r][c] = 1 # 还原A中此处的砖头，A之前是不考虑hits处有砖的grid,必须要还原，我们是在A上计算的，也就是说hits中后面的会影响前面的
                ans.append(max(0, dsu.top() - pre_roof - 1)) # 变化后状态-变化前的状态-当前砖块的1,因为这个砖是hits加上去的
        return ans[::-1] # 结果反转，因为前面hit是反转的

if __name__ == "__main__":
    a=eval(input())
    b=eval(input())
    s = Solution()
    print(s.hitBricks(a,b))