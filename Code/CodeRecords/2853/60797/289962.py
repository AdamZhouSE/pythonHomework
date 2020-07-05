class Solution:
    def find(self, n, data):
        re = 0
        total = sum(data)
        for i in range(n):
            if (total - data[i]) % 2 == 0:
                re += 1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
