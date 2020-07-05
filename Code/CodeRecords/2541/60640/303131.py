class Solution:
    def findOrder(self, numCourses, prerequisites):
        def dfs(i, adj, flag, res):
            if flag[i] == 1:
                return True
            elif flag[i] == -1:
                return False
            flag[i] = -1
            for j in adj[i]:
                if not dfs(j, adj, flag, res):
                    return False
            flag[i] = 1
            res.append(i)
            return True

        adj = [[] for _ in range(numCourses)]
        flag = [0] * numCourses
        for p in prerequisites:
            adj[p[1]].append(p[0])
        res = []
        for i in range(numCourses):
            if not dfs(i, adj, flag, res):
                return []
        return res[::-1]


if __name__ == "__main__":
    v = int(input())
    e = eval(input())
    s = Solution()
    print(s.findOrder(v, e))

