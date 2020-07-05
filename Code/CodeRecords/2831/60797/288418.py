class Solution:
    def find(self, n, data, s, t):
        re = 0
        s -= 1
        t -= 1
        total = sum(data)
        tmp1 = 0
        for i in range(s,t):
            tmp1 += data[i]
        tmp2 = total - tmp1
        if tmp1>tmp2:
            re = tmp2
        else:
            re = tmp1
        return re

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    [s,t] = [int(a) for a in input().split()]
    so = Solution()
    re = so.find(n, data, s, t)
    print(re)
