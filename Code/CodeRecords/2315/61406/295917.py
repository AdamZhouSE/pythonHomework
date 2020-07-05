class TreeNode:
    def __init__(self,value):
        self.value = value
        self.lch = None
        self.rch = None

    def set_son(self,son):
        if self.lch is None:
            self.lch = son
        else:
            self.rch = son

    def findnode(self,node,key):
        result = None
        if node.value==key:
            return node
        else:
            if node.lch is None and node.rch is None:
                return None
            if node.lch is not None:
                result = self.findnode(node.lch,key)
            if node.rch is not None and result is None:
                result = self.findnode(node.rch,key)
            return result

    def treeheight(self,node,heights,height):
        if node.lch is None and node.rch is None:
            height+=1
            heights.append(height)
            return
        if node.lch is not None:
            height+=1
            self.treeheight(node.lch,heights,height)
            height-=1
        if node.rch is not None:
            height+=1
            self.treeheight(node.rch,heights,height)
            height-=1
        return


n = int(input())
root = TreeNode(0)
for a in range(0,n-1):
    row = input().split(' ')
    node = root.findnode(root,int(row[0]))
    node.set_son(TreeNode(int(row[1])))
heights = []
root.treeheight(root,heights,0)
print(max(heights))
