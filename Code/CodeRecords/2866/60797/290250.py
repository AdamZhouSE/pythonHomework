class Solution:
    def find(self, n, data):
        re = 1
        count = 0
        sign = 0
        for i in range(n):
            if data[i]==0:
                count += 1
            else:
                if sign == 0:
                    sign = 1
                else:
                    re *= count+1
                    count = 0
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)

