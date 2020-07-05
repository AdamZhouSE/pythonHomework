class Solution:
    def find(self, n):
        re = []
        while n:
            s = n//-2
            r = n % -2
            re = re + [r]
            n = s
        return str(re.reverse())


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
