class Solution:
    def find(self, n, data):
        re = [0 for i in range(n)]
        for i in range(n):
            re[data[i]-1] = i
        return re

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    for i in range(len(re) - 1):
        print(re[i]+1, end=' ')
    print(re[len(re) - 1]+1)
