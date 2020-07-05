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

ss=input().replace('[','').replace(']','').split(',')
root=gen_tree(None,ss,0)

def solve(root):
    if not root:
        return 0
    if not root.left:
        return solve(root.right) + 1
    if not root.right:
        return solve(root.left) + 1
    return min(solve(root.left), solve(root.right)) + 1
print(solve(root))
