class Solution:
    '''
    def generate(self, start, n, k):
        global res
        res = 0
        if k == 0:
            res += 1
            return
        tmp = start
        while tmp <= n:
            self.generate(tmp, n, k - 1)
            tmp *= start
        isover = 1
        return

    def find(self, n, k):
        start = 1
        global isover
        isover = 0
        while isover != 1:
            if start > n:
                break
            self.generate(start, n, k)
            start += 1
        return res % 1000000007
    '''

    MOD = 1000000007
    def dp(self, start, n, k, res):
        global MOD
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


if __name__ == '__main__':
    [n, k] = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, k)
    print(re)
