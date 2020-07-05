class Solution:
    def shortest_path(self, n, path_blue, path_red):
        adj_blue = [[] for _ in range(n)]
        adj_red = [[] for _ in range(n)]
        for cp in path_blue:
            adj_blue[cp[0]].append(cp[1])
        for cp in path_red:
            adj_red[cp[0]].append(cp[1])
        # print(adj_red, adj_blue)
        # 从红线出发和从蓝线出发
        ans = [[1 << 31 for _ in range(2)] for _ in range(n)]

        final_ans = []
        ans[0][0] = 0
        ans[0][1] = 0
        # print(ans)

        Solution().dfs(ans, 0, 0, adj_blue, adj_red)  # 红线出发
        Solution().dfs(ans, 1, 0, adj_blue, adj_red)  # 蓝线出发

        for i in range(n):
            res = min(ans[i][0], ans[i][1])
            if res == 1 << 31:
                final_ans.append(-1)
            else:
                final_ans.append(res)
        return final_ans

    def dfs(self, ans, color, start, adj_blue, adj_red):
        adj = (adj_blue if color == 1 else adj_red)
        for j in adj[start]:
            # 判断 0 -> i -> j 的长度是否 比 已有的 0 -> j 的路径长度长 若是 则更新
            if ans[start][color] + 1 < ans[j][abs(color-1)]:
                ans[j][abs(color - 1)] = ans[start][color] + 1
                Solution().dfs(ans, abs(color-1), j, adj_blue, adj_red)


if __name__ == "__main__":
    s = Solution()
    N = int(input())
    path1 = eval(input())
    path2 = eval(input())
    print(s.shortest_path(N, path2, path1))