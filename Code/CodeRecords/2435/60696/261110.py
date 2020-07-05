"""
线段树, 复杂度O(log(n)),建树,搜索,避免重复运算
"""


class Tree:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.s = ''


# 全局变量
n = 0
m = 0
tree = [Tree()]


# 建树
def build(root, l, r):
    tree[root].l = l
    tree[root].r = r
    if l == r:
        tree[root].s = input()
        return
    mid = (l + r) >> 1
    build(root<<1 , l, mid)
    build((root<<1)|1, mid+1, r)
    if tree[root<<1].s.lower() > tree[root<<1|1].s.lower():
        tree[root].s = tree[root<<1].s
    else:
        tree[root].s = tree[root<<1|1].s


# 查询
def query(root, l, r):
    if l <= tree[root].l and tree[root].r <= r:
        return root
    mid = (tree[root].l + tree[root].r) >> 1
    if r <= mid:
        return query(root<<1, l, r)
    elif mid < l:
        return query(root<<1|1, l, r)
    else:
        a = query(root<<1, l, mid)
        b = query(root<<1|1, mid + 1, r)
        if tree[a].s.lower() > tree[b].s.lower():
            return a
        else:
            return b


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    n = arr[0]
    m = arr[1]
    tree = [Tree() for i in range(pow(2,n))]
    build(1, 1, n)
    for i in range(m):
        arr = [int(j) for j in input().split()]
        l = arr[0]
        r = arr[1]
        print(tree[query(1, l, r)].s)