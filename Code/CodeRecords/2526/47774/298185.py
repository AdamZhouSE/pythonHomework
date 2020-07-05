from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def gen_tree(root,list,i):
    if i<len(list):
        if list[i]=='null':
            return None
        else:
            root=TreeNode(list[i])
            root.left=gen_tree(root.left,list,2*i+1)
            root.right=gen_tree(root.right,list,2*i+2)
            return root
    return root

s1=input().replace('[','').replace(']','').split(',')
s2=input().replace('[','').replace(']','').split(',')
ss1=[]
ss2=[]
for i in s1:
    if i>='0' and i<='9':
        ss1.append(int(i))
    else:
        ss1.append(i)
for i in s2:
    if i>='0' and i<='9':
        ss2.append(int(i))
    else:
        ss2.append(i)
root1=gen_tree(None,ss1,0)
root2=gen_tree(None,ss2,0)

res = []
def solve(root):
    if root:
        solve(root.left)
        res.append(root.val)
        solve(root.right)
        
solve(root1)
solve(root2)
print(sorted(res))