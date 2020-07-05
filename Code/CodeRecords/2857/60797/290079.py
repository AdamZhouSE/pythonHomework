import math


class Solution:
    def gcd(self, a, b):
        s = a + b
        a = max(a, b)
        b = s - a
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    def find(self, n, data):
        re = 0
        tmp = data[0]
        for i in range(n):
            tmp = self.gcd(tmp, data[i])
        for i in range(1, int(math.sqrt(tmp))+1):
            if tmp % i == 0:
                re += 1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
