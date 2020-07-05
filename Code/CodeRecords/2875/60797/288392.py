class Solution:
    def find(self, n, data):
        map = [0 for i in range(n)]
        for i in range(n):
            map[data[i]] = i


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    for item in re:
        print(item, end=' ')
