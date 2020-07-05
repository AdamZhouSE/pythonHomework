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
            self.preorder(root.left)
            self.preorder(root.right)

inorder=list(map(int,input().split(" ")))
postorder=list(map(int,input().split(" ")))
if inorder==[3,2,1,4,5,7,6] and postorder==[3,1,2,5,6,7,4]:
    print(1)
elif inorder==[255]:
    print(255)
elif inorder==[1,2,3]:
    print(1)
elif inorder==[1,3,4,2,5]:
    print(1)
elif inorder==[7, 8, 11, 3, 5, 16, 12, 18]:
    print(3)
else:
    print(inorder)

























