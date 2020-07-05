class Solution:
    def numberOfWays(self, n: int) -> int:
        res = 1
        for i in range(1, n // 2 + 1):
            res *= n - i + 1
            res //= i
        return res // (n // 2 + 1) % (10**9 + 7)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        num = int(num/2) * 2
        print(Solution().numberOfWays(num))