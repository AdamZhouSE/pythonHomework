class Solution:
    def find(self, n, data):
        re=0
        for item in data:
            if item>0:
                re += item - 1
            elif item<0:
                re += -1 - item
            else:
                re += 1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
