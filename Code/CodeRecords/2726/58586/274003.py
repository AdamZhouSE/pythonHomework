class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def arrToTree(self,arr):
        if len(arr)==0:
            return None
        if arr[0]=="null":
            return None
        root=TreeNode(int(arr[0]))
        idx=0
        queue=[root]
        while len(queue)>0 or idx<len(arr):
            size=len(queue)
            for i in range(size):
                node = queue.pop()
                idx += 1
                if idx<len(arr):
                    if arr[idx]=="null":
                        node.left=None
                    else:
                        left=TreeNode(int(arr[idx]))
                        node.left = left
                        queue.insert(0, left)
                else:
                    break
                idx+=1
                if idx<len(arr):
                    if arr[idx] == "null":
                        node.right = None
                    else:
                        right = TreeNode(int(arr[idx]))
                        node.right = right
                        queue.insert(0, right)
        return root
arr=input().replace("[","").replace("]","").split(",")
s=Solution()
root=s.arrToTree(arr)
ans=[10000007]
shortest=[10000007]
def dfs(root:TreeNode,depth,pathSum):
    pathSum+=root.val
    if root.left==None and root.right==None:
        if pathSum<shortest[0]:
            shortest[0]=pathSum
            ans[0]=min(ans[0],depth)
        return
    dfs(root.left,depth+1,pathSum)
    dfs(root.right,depth+1,pathSum)
dfs(root,1,0)
print(ans[0])