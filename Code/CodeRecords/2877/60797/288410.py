class Solution:
    def find(self, n, data):
        sum = 0
        for item in data:
            sum = sum + abs(item)
        return sum

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
