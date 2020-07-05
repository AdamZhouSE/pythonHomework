class Solution:

    '''
    def dp(self, start, n, k, res):
        MOD = 1000000007
        if k == 0:
            res += 1
            res = res % MOD
        else:
            for i in range(start, n + 1, start):
                res = self.dp(i, n, k - 1, res)
        return res

    def find(self, n, k):
        res = 0
        for i in range(1, n + 1):
            res = self.dp(i, n, k - 1, res)
        return res
    '''

    def find(self, n, k):
        re = 0
        m = [[0 for i in range(n+1)] for i in range(k+1)] # m[a][b] a为k的值，b为子序列的第一个值
        for i in range(1,n+1):
            m[1][i] = 1
        for i in range(2, k+1):
            for j in range(1, n+1):
                for t in range(j, n+1, j):
                    m[i][j] = m[i-1][t]
        for item in m[k]:
            re += item
        return re


if __name__ == '__main__':
    [n, k] = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, k)
    print(re)
