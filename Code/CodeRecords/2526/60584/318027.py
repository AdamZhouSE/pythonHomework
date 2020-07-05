class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
    l = []
    self.getroot(root1, l)  
    self.getroot(root2, l)  
    l.sort()
    return l

def getroot(self, root: TreeNode, l: List[int]):
    if root:
        l.append(root.val) 
        self.getroot(root.left, l)
        self.getroot(root.right, l)
    else:
        return