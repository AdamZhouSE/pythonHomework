class Tree():
    k = 0

    def __init__(self, ltree=0, rtree=0, data=0, father=0):
        self.ltree = ltree
        self.rtree = rtree
        self.data = data
        self.fatree = father

    def inorder(self, root):
        if treeNode[root].ltree != 0:
            self.inorder(treeNode[root].ltree)
        self.k += 1
        inord[self.k] = treeNode[root].data - self.k
        if treeNode[root].rtree != 0:
            self.inorder(treeNode[root].rtree)

    def lower_bound(self, arr, target, i, j):
        while i < j:
            mid = i + (j - i) / 2
            mid = int(mid)
            if target > arr[mid]:
                i = mid + 1
            else:
                j = mid
        return mid


if __name__ == "__main__":
    num = int(input())
    lis = [None] * (num + 1)
    inord = [None] * (num + 1)
    treeNode = [None] * (num + 1)
    m = list(map(int, input().strip().split()))
    tree = Tree()
    for i in range(1, num + 1):
        if i != 1:
            treeNode[i] = Tree(data=m[i - 1])
        else:
            treeNode[1] = Tree(data=m[i - 1], father=0)
    for i in range(2, num + 1):
        a, b = map(int, input().strip().split())
        treeNode[i].fatree = a
        if b == 0:
            treeNode[treeNode[i].fatree].ltree = i
        else:
            treeNode[treeNode[i].fatree].rtree = i
    tree.inorder(1)
    lis[1] = inord[1]
    cnt = 1
    for i in range(2, num + 1):

        if inord[i] > lis[cnt]:
            lis[++cnt] = inord[i]
        else:
            for k in range(1, 1 + cnt):
                if lis[k] >= inord[i]:
                    j = k
                    break
            lis[j] = inord[i]
    print(num - cnt)
