class Solution:
    def dp(self, start, n, k):
        global res
        if k == 0:
            res += 1
            res = res % MOD
        else:
            for i in range(start, n + 1, start):
                self.dp(i, n, k - 1)

    def find(self, n, k):
        res = 0
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
