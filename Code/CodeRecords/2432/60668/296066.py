class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def build(inorder=[],postorder=[]):
    if not inorder:
         return None
    root = TreeNode(postorder[-1])
    i = inorder.index(root.val)
    root.left = build(inorder[:i],postorder[:i])
    root.right =build(inorder[i+1:],postorder[i:-1])
    return root
def find(nowNum,root):
    if root.left==None and root.right==None:
        return [nowNum+int(root.val),int(root.val)]
    elif root.left==None:
        return find(nowNum+int(root.val),root.right)
    elif root.right==None:
        return find(nowNum+int(root.val),root.left) 
    else:
        num1 = find(nowNum+int(root.val),root.left)
        num2 = find(nowNum+int(root.val),root.right)
        if num1[0]>num2[0]:
            return num2
        else:
            return num1
if __name__=='__main__':
    inorder = [int(i) for i in input().split()]
    postorder = [int(i) for i in input().split()]
    root=build(inorder,postorder)
    print(find(0,root)[1])