# LeetCode 310

class Solution:
    def findMinHeightTrees(self, n, edges):
        g = dict()
        degrees = [0] * n  
        for f, t in edges:
            degrees[f] += 1
            degrees[t] += 1
            if f in g:
                g[f].append(t)
            else:
                g[f] = [t]
            if t in g:
                g[t].append(f)
            else:
                g[t] = [f]
        leaves = []
        for i in range(n):
            if degrees[i] == 1:
                leaves.append(i)
        res = set(range(n))
        while len(res) > 2:
            new_leaves = []
            for leaf in leaves:
                res.remove(leaf)
                for node in g[leaf]:
                    if node in res:
                        degrees[node] -= 1
                        if degrees[node] == 1:
                            new_leaves.append(node)
            leaves = new_leaves
        return list(res)

n = eval(input())
lst = eval(input())
s = Solution()
print(s.findMinHeightTrees(n, lst))