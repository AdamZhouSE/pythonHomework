class Solution:
    def find(self, n, data):
        days = 0
        for i in range(n):
            if data[i] == i:
                days += 1
        return days

if __name__ == '__main__':
    n = int(input())
    data = [int(a) - 1 for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
