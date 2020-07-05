class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution:
    def minDepth(self, root):
        
        children = []
        lft=root*2+1
        rht=root*2+2
        if(lft<len(t)):
            if(t[lft]!='null'):
                children.append(int(t[lft]))
            if(rht<len(t)):
                if(t[rht]!='null'):
                    children.append(int(t[rht]))
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1 
t=list(input().replace('[','').replace(']','').split(','))
print(Solution().minDepth(0))