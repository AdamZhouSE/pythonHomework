class TreeNode(object):

    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
        
class solution(object):
    def buildTree(self,inorder,postorder):
        if len(inorder)==0 or len(postorder)==0:
            return
        else:
            root=TreeNode(postorder[-1])
            index_=inorder.index(root.val)
            left_inorder,left_postorder=inorder[:index_],postorder[:index_]
            right_inorder,right_postorder=inorder[index_+1:],postorder[index_:-1]
            root.left = self.buildTree(left_inorder,left_postorder)
            root.right = self.buildTree(right_inorder,right_postorder)
            return root

class traverse:        
    def preorder(self,root):
        if root==0:
            return
        else:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

inorder=list(map(int,input().split(" ")))
postorder=list(map(int,input().split(" ")))
tree=solution()
root=tree.buildTree(inorder,postorder)
t=traverse()
t.preorder(root)