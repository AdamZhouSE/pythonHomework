class Solution:
    def find(self, n, m, a):
        re = 0
        while m > 0:
            m = m - max(a)
            a.remove(max(a))
            re += 1
        return re

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))
    s = Solution()
    re = s.find(n, m, data)
    print(re)
