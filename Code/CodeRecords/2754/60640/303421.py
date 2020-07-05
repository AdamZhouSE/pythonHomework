class Solution:
    def find_max(self, matrix):
        ans = -1
        num1 = 0
        num0 = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                if matrix[i][j] == 1:
                    num1 += 1
                if matrix[i][j] == 0:
                    num0 += 1
        if num1 == m * n or num0 == m * n:
            return ans
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans = max(Solution().count(matrix, i, j), ans)
        return ans

    def count(self, matrix, x, y):
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    ans.append(abs(x-i)+abs(y-j))
        ans.sort()
        return ans[0]


if __name__ == "__main__":
    s = Solution()
    inp = eval(input())
    res = s.find_max(inp)
    print(res)
