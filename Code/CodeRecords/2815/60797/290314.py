class Solution:
    def find(self, n, data):
        re=0
        count = 0
        for item in data:
            if item>0:
                re += item - 1
            elif item<0:
                re += -1 - item
                count += 1
            else:
                if count:
                    count -= 1
                re += 1
        if count%2!=0:
            re += 2
        return re


if __name__ == '__main__':
    n = 22
    data = [-77, 0, 99, 66, -2, 82, 59, 67, 92, -19, -37, 20, 81, 41, 65, -82, 60, 30, 43, -10, 63, -21]
    s = Solution()
    re = s.find(n, data)
    print(re)
