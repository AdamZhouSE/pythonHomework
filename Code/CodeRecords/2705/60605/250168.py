# 题目描述
# 在本问题中，有根树指满足以下条件的有向图。
# 该树只有一个根节点，所有其他节点都是该根节点的后继。
# 每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
# 附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。
# 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u and v和顶点的边，其中父节点u是子节点v的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。
# 若有多个答案，返回最后出现在给定二维数组的答案。
#
# 二维数组大小的在3到1000范围内。
#
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

import collections

def union(li, set1, set2):
    if set1 == set2: return
    li[set1] += li[set2]
    li[set2] = set1

def find(li, start) -> int:
    while li[start] >= 0:
        start = li[start]
    return start

def isConnected(li: list, maxPoint : int, ignored: list) :
    ufs = [-1 for i in range(maxPoint)]
    for i in li:
        if i == ignored: continue
        a0 = i[0]-1
        a1 = i[1]-1
        union(ufs, find(ufs, a0), find(ufs, a1))
    cnt = 0
    for i in ufs:
        if i < 0:
            cnt += 1
            if cnt > 1:
                return False
    return True

def solve() :
    li = list(eval(input()))
    # li = [[1, 2], [1, 3], [2, 3]]
    # print(li)

    # Get all points
    maxPoint = 0
    for i in li:
        maxPoint = max(maxPoint, i[0])
        maxPoint = max(maxPoint, i[1])

    inList = []
    for i in li:
        inList.append(i[1])
    li.reverse()
    c = collections.Counter(inList)
    c = sorted(c.items(), key=lambda vi: vi[1], reverse=True)
    if c[0][1] == 2:
        # 无环形
        target = c[0][0]
        tarli = []
        for j in li:
            if j[1] == target:
                tarli.append(j)
        for j in li:
            if j in tarli:
                return j
    else:
        # 有环形
        for ignored in li:
            if isConnected(li, maxPoint, ignored):
                return ignored
        pass


if __name__ == '__main__':
    print(solve())
