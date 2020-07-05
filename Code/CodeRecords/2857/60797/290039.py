import math

class Solution:
    def find(self, n, data):
        re = 0
        maxnum = max(data)
        end = int(math.sqrt(maxnum))
        for i in range(1,end+1):
            isvalid = 1
            for item in data:
                if data/i!=0:
                    isvalid = 0
                    break
            if isvalid==1:
                re+=1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
