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

    res = 0

    def dp(self, start, n, k):
        global res
        if k == 0:
            res += 1
            res = res % MOD
        else:
            for i in range(start, n + 1, start):
                self.dp(i, n, k - 1)

    def find(self, n, k):
        for i in range(1, n + 1):
            self.dp(i, n, k - 1)
        return res


if __name__ == '__main__':
    [n, k] = [int(a) for a in input().split()]
    global MOD
    MOD = 1000000007
    s = Solution()
    re = s.find(n, k)
    print(re)
