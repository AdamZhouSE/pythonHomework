from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            # 方法一
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and \
                        matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            lookup[i][j] = max(res, lookup[i][j])
            # 方法二
            # val = matrix[i][j]
            # lookup[i][j] = 1 + max(
            #     dfs(i + 1, j) if 0 <= i + 1 < row and 0 <= j < col and matrix[i + 1][j] > val else 0,
            #     dfs(i - 1, j) if 0 <= i - 1 < row and 0 <= j < col and matrix[i - 1][j] > val else 0,
            #     dfs(i, j + 1) if 0 <= i < row and 0 <= j + 1 < col and matrix[i][j + 1] > val else 0,
            #     dfs(i, j - 1) if 0 <= i < row and 0 <= j - 1 < col and matrix[i][j - 1] > val else 0,
            # )
            # 方法三
            # lookup[i][j] = 1 + max(
            #     [dfs(i + x, y + j) for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]] \
            #      if 0 <= (i + x) < row and 0 <= (j + y) < col and matrix[i + x][j + y] > matrix[i][j]] or [0]
            # )

            return lookup[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))


if __name__ == "__main__":
    lines = ""
    while True:
        try:
            lines += (input().strip())
        except:
            break
    lines = eval(lines)
    solution = Solution()
    result = solution.longestIncreasingPath(lines)
    print(result)
