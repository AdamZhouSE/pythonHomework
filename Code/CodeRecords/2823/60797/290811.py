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
        m = [[0 for i in range(n)] for i in range(k)] # m[a][b] a为k的值-1，b为子序列的第一个值-1
        for i in range(n):
            m[0][i] = 1
        for i in range(1, k):
            for j in range(n):
                for t in range(j,n,j):
                    m[i][j] = m[i-1][t]
        for item in m[k-1]:
            re += item
        return re


if __name__ == '__main__':
    [n, k] = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, k)
    print(re)
