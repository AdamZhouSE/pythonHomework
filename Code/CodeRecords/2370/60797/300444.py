class Solution:
    def find(self, n):
        re = []
        while n:
            n = n//-2
            s = n % -2
            re = re + [s]
        return str(re.reverse())


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
