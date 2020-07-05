import ast
class Solution:
    def get(self, root1, root2):
        ans = list()

        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root1)
        dfs(root2)
        ans.sort()
        return ans


s1=input()
s2=input()
q=Solution()
res=q.get(s1,s2)
print(res)
