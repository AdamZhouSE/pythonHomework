maxSum=2**32
leave_Val=0
class Node(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class solution(object):
    def buildtree(self,inorder,postorder):
        if len(inorder)==0 or len(postorder)==0:
            return
        else:
            root=Node(postorder[-1])
            idx=inorder.index(root.val)
            left_in=inorder[:idx]
            left_post=postorder[:idx]
            right_in=inorder[idx+1:]
            right_post=postorder[idx:-1]
            root.left=self.buildtree(left_in,left_post)
            root.right=self.buildtree(right_in,right_post)
            return root

def dfs(root,sum):
    global maxSum
    global leave_Val
    sum+=root.val
    if root.left==None and root.right==None:
        if sum<maxSum:
            maxSum=sum
            leave_Val=root.val
    else:
        if root.left!=None:
            dfs(root.left,sum)
        if root.right!=None:
            dfs(root.right,sum)

if __name__=='__main__':
    sol=solution()
    inorder=list(map(int,input().split(" ")))
    postorder=list(map(int,input().split(" ")))
    root=sol.buildtree(inorder,postorder)
    dfs(root,0)
    print(leave_Val)
