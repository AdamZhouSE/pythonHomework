class Solution:
    def find(self, n, data):
        for item in data:
            re = re + abs(item)
        return re

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
