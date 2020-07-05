class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def helper(left,right):
    global preorder
    global inorderIdxMap
    if left>right: return None
    rootVal=preorder.popleft()
    root=TNode(rootVal)
    idx=inorderIdxMap[rootVal]
    root.left=helper(left,idx-1)
    root.right=helper(idx+1,right)
    return root

def printPostorder(root):
    if root:
        if root.left: printPostorder(root.left)
        if root.right: printPostorder(root.right)
        print(root.val,end='')
        

from collections import deque
while True:
    try:
        line1=input()
        preorder=deque(line1)

        line2=input()
        inorder=deque(line2)
        inorderIdxMap={nodeVal:idx for idx,nodeVal in enumerate(inorder)}

        root=helper(0,len(preorder)-1)
        printPostorder(root)
        print()
    except:
        break