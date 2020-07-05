maxlen = 0


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def setl(self, data):
        self.left = data
    
    def getl(self):
        return(self.left)
    
    def setr(self, data):
        self.right = data
    
    def getr(self):
        return(self.right)
    
    def setv(self, data):
        self.data = data
        
    def getv(self):
        return self.data
    

class Tree:
    def __init__(self):
        self.nodes = {}

    
def crTree(mat):
    tree = Tree()
    for st in mat:
        fa = st[0]
        lch = st[1]
        rch = st[2]
        val = st[3]
        if fa and (fa not in tree.nodes):
            tree.nodes[fa] = TreeNode(fa)
        if lch and (lch not in tree.nodes):
            tree.nodes[lch] = TreeNode(lch)
        if rch and (rch not in tree.nodes):
            tree.nodes[rch] = TreeNode(rch)
        fan = tree.nodes[fa]
        fan.setv(val)
        if lch:
            ln = tree.nodes[lch]
            fan.left = ln
        if rch:
            rn = tree.nodes[rch]
            fan.right = rn
    return tree


def preO(head, summ, presum, level, summap):
    global maxlen
    if head==None:
        return maxlen
    
    cursum = presum + head.getv()
    if not summap.__contains__(cursum):
        summap[cursum] = level
    if summap.__contains__(cursum-summ):
        maxlen = max(maxlen, level-summap[cursum-summ])

    presum=cursum
    preO(head.left, summ, presum, level+1, summap)
    preO(head.right, summ, presum, level+1, summap)

    if level==summap[cursum]:
        del summap[cursum]

    return maxlen


if __name__ == "__main__":
    summap = {0:0}
    c1 = [int(i) for i in input().split( )]
    n, head = c1[0], c1[1]
    mat = []
    while n:
        cmd = [int(i) for i in input().split( )]
        mat.append(cmd)
        n -= 1
    tree = crTree(mat)
    summ = int(input())
    ans = preO(tree.nodes[head], summ, 0, 1, summap)
    print(ans)
    