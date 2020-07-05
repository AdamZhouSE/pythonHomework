class Solution:
    def find(self, n):
        for i in range(n):
            if '0' not in str(i) and '0' not in str(n-i):
                re = [i,n-i]
                return re


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
