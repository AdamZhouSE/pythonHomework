import sys
class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]
        ans = 0

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            lookup[i][j] = max(res, lookup[i][j])

        return max(dfs(i, j) for i in range(row) for j in range(col))


if __name__ == "__main__":
    lines=""
    while True:
        try:
            lines.extend(input())
        except:
            break
    lines = eval(lines)
    solution = Solution()
    result = solution.longestIncreasingPath(lines)
    print(result)
