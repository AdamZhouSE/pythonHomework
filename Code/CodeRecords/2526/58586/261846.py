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
ans=[]
def inorder(root:TreeNode):
    if root==None:
        return
    inorder(root.left)
    ans.append(root.val)
    inorder(root.right)
s=Solution()
p_raw=input().replace("[","").replace("]","")
p_arr=[]
if len(p_raw)>1:
    p_arr=p_raw.split(",")
else:
    p_arr=p_raw.split()
p=s.arrToTree(p_arr)
q_raw=input().replace("[","").replace("]","")
q_arr=[]
if len(q_raw)>1:
    q_arr=q_raw.split(",")
else:
    q_arr=q_raw.split()
q=s.arrToTree(q_arr)
inorder(p)
inorder(q)
ans.sort()
print(ans)

