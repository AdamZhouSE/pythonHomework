class Solution:
    def find(self, n, data):
        re=0
        a = data.count(1)
        b = data.count(2)
        c = data.count(3)
        d = data.count(4)
        re += d
        d = 0
        if a >= c:
            a = a - c
            re += c
            c = 0
        else:
            c = c-a
            re += a
            a = 0
            re += c
        re += int(b/2)
        b = b%2
        if 2*b<=a:
            a = a-2*b
            re += b
            b = 0
            re += int(a/4)
            a=0
        else:
            re+=b
            b = 0
            a=0
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
