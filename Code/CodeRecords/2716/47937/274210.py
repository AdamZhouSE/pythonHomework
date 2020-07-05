from typing import List
class Solution:

    def dfs(self, i, j, k, all_nodes, visited, m, n):
        if (i, j, k) in visited:
            return

        if (i, j, k) not in all_nodes:
            return

        direc = [
            [],
            [[0, -1, [2, 4, 5]], [-1, 0, [2, 3, 5]]],
            [[0, 1, [1, 3, 5]], [1, 0, [1, 4, 5]]],
            [[0, -1, [2, 4, 5]], [1, 0, [1, 4, 5]]],
            [[0, 1, [1, 3, 5]], [-1, 0, [2, 3, 5]]],
            [ [0, 1, [1, 3, 5]], [-1, 0, [2, 3, 5]], [0, -1, [2, 4, 5]], [1, 0, [1, 4, 5]] ]
        ]

        visited.add((i, j, k))
        for delta_i, delta_j, next_stat in direc[k]:
            new_i, new_j = i + delta_i, j + delta_j
            if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n:
                for new_k in next_stat:
                    self.dfs(new_i, new_j, new_k, all_nodes, visited, m, n)


    def regionsBySlashes(self, grid: List[str]) -> int:
        all_nodes = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    all_nodes.add((i, j, 1))
                    all_nodes.add((i, j, 2))
                elif grid[i][j] == '\\':
                    all_nodes.add((i, j, 3))
                    all_nodes.add((i, j, 4))
                else:
                    all_nodes.add((i, j, 5))

        visited = set()
        cnt = 0
        for node in all_nodes:
            if node not in visited:
                cnt += 1
                self.dfs(node[0], node[1], node[2], all_nodes, visited, m, n)

        return cnt
    
