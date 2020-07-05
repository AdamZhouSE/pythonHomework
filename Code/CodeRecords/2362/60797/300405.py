class Solution:
    def find(self, n):
        re = 0
        tmp = 0
        for i in range(n,0,-4):
            if i>2:
                tmp = int(i*(i-1)/(i-2))
                if i==n:
                    re += tmp
                else:
                    re -= tmp
                re += i-3
            else:
                tmp = i
                if i==n:
                    re += tmp
                else:
                    re -= tmp
        return re


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
