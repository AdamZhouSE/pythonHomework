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
root1=gen_tree(None,s1,0)
root2=gen_tree(None,s2,0)

res = []
def solve(root):
    if root:
        solve(root.left)
        res.append(root.val)
        solve(root.right)
        
solve(root1)
solve(root2)
res=sorted(res)
print('[',end='')
for i in range(len(res)):
    if i==0:
        print(int(res[i]),end='')
    else:
        print(', ',int(res[i]),end='',sep='')
print(']')
    