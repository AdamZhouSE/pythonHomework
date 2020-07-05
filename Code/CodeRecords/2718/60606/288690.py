class UnionFind:
    '''
    parent[i]表示的含义为，索引为i的节点，它的直接父节点为parent[i]。初始化时各个节点都不相连，因此初始化parent[i]=i，让自己成为自己的父节点，从而实现各节点不互连
    '''

    def __int__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    '''
    由于parent[i]仅表示自己的直接父节点，查询两个节点是否相交需要比较它们的根节点是否相同。因此要封装一个查询自己根节点的方法
    '''

    def get_root(self, i):
        if self.parent[i] != self.parent[self.parent[i]]:
            self.parent[i] = self.get_root(self.parent[i])
        return self.parent[i]

    def is_connected(self, i, j):
        return self.get_root(i) == self.get_root(j)

    def union(self, i, j):
        i_root = self.get_root(i)
        j_root = self.get_root(j)
        self.parent[j_root] = i_root

def handle(s,l):
    #先整体排序，再按顺序填到原数组里
    temp = ""
    for item in l:
        temp += s[item]
    temp = list(temp)
    temp.sort()
    for i in range(len(l)):
        s[l[i]] = temp[0]
        temp.remove(temp[0])
#实际上可以将整个问题看成一张图，每一个连通分量中进行排序

s = list(input())
#建立并查集
union = UnionFind()
union.__int__(len(s))
pair = input()[2:-2].split("],[")
for i in range(len(pair)):
    temp = pair[i].split(",")
    x = int(temp[0])
    y = int(temp[1])
    union.union(x,y)
index = [[] for i in range(len(s))]#i位置对应并查集中挂到i上的下标
for i in range(len(s)):
    index[union.get_root(i)].append(i)
#模块化处理排序
for i in range(len(index)):
    handle(s,index[i])
print("".join(s))

