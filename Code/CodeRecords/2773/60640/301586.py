class Solution:
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    m = int()
    n = int()

    def longest_path(self, matrix):
        if len(matrix) == 0:
            return 0
        # 使用类变量，可以用类名.变量名
        Solution.m = len(matrix)
        Solution.n = len(matrix[0])
        ans = 0
        cache = [[0 for _ in range(Solution.n)] for _ in range(Solution.m)]
        for i in range(Solution.m):
            for j in range(Solution.n):
                ans = max(ans, Solution().dfs(matrix, i, j, cache))
        return ans

    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0:
            return cache[i][j]

        for d in Solution.dirs:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < Solution.m and 0 <= y < Solution.n and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], Solution().dfs(matrix, x, y, cache))
        cache[i][j] += 1
        return cache[i][j]


if __name__ == "__main__":
    matrix_inp = []
    try:
        while True:
            inp = input()
            line = []
            for c in inp:
                if c.isdigit():
                    line.append(int(c))
            if len(line) > 0:
                matrix_inp.append(line)
    except EOFError:
        s = Solution()
        res = s.longest_path(matrix_inp)
        print(res)
