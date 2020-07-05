class Solution:
    def maxsubsum(self, a):
        re = 0
        count = 0
        for i in range(len(a)):

            if a[i] == 0:
                re = max(re, count)
                count = 0
            else:
                count += a[i]
        re = max(re, count)
        return re

    def find(self, a, d):
        re = []
        for i in range(n):
            a[d[i]-1] = 0
            re.append(self.maxsubsum(a))
        return re


if __name__ == '__main__':
    n = int(input())
    a = [int(a) for a in input().split()]
    d = [int(a) for a in input().split()]
    s = Solution()
    res = s.find(a, d)
    for item in res:
        print(item)
