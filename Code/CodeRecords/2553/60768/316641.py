class Tree:
    fa = -1;
    l = -1
    r = -1

    def __init__(self, faa, ll, rr):
        fa = faa
        l = ll
        r = rr


tr = [Tree(-1, -1, -1) for x in range(100005)]
w = [0 for x in range(100005)]  # 节点的数值
inord = [0 for x in range(100005)]  # 中序遍历

lis = [0 for x in range(100005)]  # 最长不降子序列


def inOrder(root: int, k: list):  # k作为list 只用第一个值，为了按引用传递
    if tr[root].l != -1:
        inOrder(tr[root].l, k)
    k[0] += 1
    inord[k[0]] = w[root] - k[0]
    if tr[root].r != -1:
        inOrder(tr[root].r, k)