class Solution:
    def find(self, n, data):
        re = 0
        data.sort()
        for i in range(0,n,2):
            re = re + data[i+1]-data[i]
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
