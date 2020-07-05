class Solution:
    def find(self, n, a, b):
        if a==0 and b!=0:
            return 0
        else:
            exp = '5' * a + '0' * b
            up = eval(exp)
            isfind = 0
            while isfind == 0:
                if up % 90==0:
                    str2 = str(up)
                    tmp = list(str2)
                    tmplength = len(tmp)
                    numof5 = tmp.count(5)
                    numof0 = tmp.count(0)
                    if numof5<=a and numof0<=b and numof0 + numof5==tmplength:
                        isfind = 1
                        return up
                up -= 1
            if b==0:
                return -1
            else:
                return 0


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    numof5 = data.count(5)
    numof0 = data.count(0)
    s = Solution()
    re = s.find(n, numof5, numof0)
    print(re)
