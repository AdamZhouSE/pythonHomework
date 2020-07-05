class Solution:
    def findRedundantConnection(self, edges):
        p = [i for i in range(len(edges) + 1)]
        p = [*range(len(edges) + 1)]      #并查集元素初始化
        def f(x):
            if p[x] != x:       #递归修改所属集合,看上面dsu定义
                p[x] = f(p[x])  #如果结点是它自己的父结点，我们将其称为连接结点的领导者，保证p[x]=x这就是求领导节点的函数
            return p[x]
        for x, y in edges:      #遍历边
            px, py = f(x), f(y)
            if px != py:        #检查集合，领导节点是否相同，如果集合不同就合并
                p[py] = px
            else:
                return [x, y]   #集合相同就返回答案


edges = eval(input())
s = Solution()
print(s.findRedundantConnection(edges))