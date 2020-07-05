class Solution:
    def find(self, n, x, y):
        for i in range(n):
            temp = x + y
            re = max(re, temp)
        return re
        

if __name__ == '__main__':
    n = int(input())
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    for i in range(n):
        line = [int(a) for a in input().split()]
        x[i] = line[0]
        y[i] = line[1]
    s = Solution()
    re = s.find(n, x, y)
    print(re)
