maxSum=2**32
leave_Val=0
class Node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class solution(object):
    def buildtree(self,inorder,preorder):
        if len(inorder)==0 or len(preorder)==0:
            return
        else:
            root=Node(preorder[0])
            idx=inorder.index(root.val)
            left_in=inorder[:idx]
            left_pre=preorder[1:idx+1]
            right_in=inorder[idx+1:]
            right_pre=preorder[idx+1:]
            root.left=self.buildtree(left_in,left_pre)
            root.right=self.buildtree(right_in,right_pre)
            return root

def post_order(root):
    if root.left:
        post_order(root.left)
    if root.right:
        post_order(root.right)
    print(root.val,end="")

if __name__=='__main__':
    sol=solution()
    while True:
        preorder=input()
        inorder=input()
        if preorder=="":
            break
        root=sol.buildtree(inorder,preorder)
        post_order(root)
        print()
    
