class Solution:

    def find(self, data):
        re = 0
        if len(data)==2:
            return re
        data.sort()
        for i in range(len(data)-1):
            re = max(re, abs(data[i]-data[i+1]))
        return re


if __name__ == '__main__':
    data = [int(a) for a in input().strip('[]').split(',')]
    s = Solution()
    re = s.find(data)
    print(re)