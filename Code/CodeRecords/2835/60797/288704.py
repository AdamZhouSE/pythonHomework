class Solution:
    def find(self, n, a, b):
        if b==0:
            return -1
        elif a<9:
            return 0
        else:
            re = '5'*(a-a%9)+'0'*b
            return eval(re)


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    numof5 = data.count(5)
    numof0 = data.count(0)
    s = Solution()
    re = s.find(n, numof5, numof0)
    print(re)
