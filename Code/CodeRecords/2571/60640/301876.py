class Solution:
    def find_max(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        res = - (1 << 31)
        for i in range(1, row+1):
            for j in range(1, col+1):
                dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
                dp[i][j] = matrix[i-1][j-1]
                for m in range(i, row+1):
                    for n in range(j, col+1):
                        dp[m][n] = dp[m-1][n] + dp[m][n-1] - dp[m-1][n-1] + matrix[m-1][n-1]
                        if dp[m][n] <= k:
                            res = max(res, dp[m][n])
        return res


if __name__ == "__main__":
    a = int(input())
    inp1 = [int(x) for x in input().split(",")]
    inp2 = [int(x) for x in input().split(",")]
    K = int(input())
    arr = [inp1, inp2]
    s = Solution()
    ans = s.find_max(arr, K)
    print(ans)