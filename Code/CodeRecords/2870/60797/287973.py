class Solution:
    def find(self, n, data):
        re = sum(data)
        data.sort()
        for i in range(n):
            if re%2==0:
                return re
            else:
                re -= data[i]

if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)

