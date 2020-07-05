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
        if fa and (fa not in tree.nodes):
            tree.nodes[fa] = TreeNode(fa)
        if lch and (lch not in tree.nodes):
            tree.nodes[lch] = TreeNode(lch)
        if rch and (rch not in tree.nodes):
            tree.nodes[rch] = TreeNode(rch)
        fan = tree.nodes[fa]
        if lch:
            ln = tree.nodes[lch]
            fan.left = ln
        if rch:
            rn = tree.nodes[rch]
            fan.right = rn
    return tree


def lowestAncestor(tree, head, o1, o2):
    if head == None or head == o1 or head == o2:
        return head
    left = lowestAncestor(tree, head.left, o1, o2)
    right = lowestAncestor(tree, head.right, o1, o2)
    if left and right:
        return head
    return left if left else right


if __name__ == "__main__":
    c1 = [int(i) for i in input().split( )]
    n, root = c1[0], c1[1]
    mat = []
    while n:
        con = [int(i) for i in input().split( )]
        mat.append(con)
        n -= 1
    c2 = [int(i) for i in input().split( )]
    o1, o2 = c2[0], c2[1]
    tree = crTree(mat)
    print(lowestAncestor(tree, tree.nodes[root], tree.nodes[o1], tree.nodes[o2]).getv())
    