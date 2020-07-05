class Solution:
    def find(self,n, data):
        re = [0 for i in range(n)]
        for i in range(len(data)):
            for j in range(data[i][0]-1,data[i][1]):
                re[j]+=data[i][2]
        return re


if __name__ == '__main__':
    t=int(input())
    data = []
    for i in range(t):
        line = [int(a) for a in input().split(',')]
        data.append(line)
    n = int(input())
    s = Solution()
    re = s.find(n,data)
    print(re)
