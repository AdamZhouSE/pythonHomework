class Solution:
    def find(self, n, data):
        re = 0
        sum = sum(data)
        for i in range(n):
            if (sum - data[i]) % 2 == 0:
                re+=1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
