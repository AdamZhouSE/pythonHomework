class Solution:
    def find(self, data):
        re = 0
        for i in range(5):
            for j in range(5):
                if data[i][j] == 1:
                    re = abs(i-3)+abs(j-3)
        return re

if __name__ == '__main__':
    data = []
    for i in range(5):
        line = input().split()
        data.append(line)
    s = Solution()
    re = s.find(data)
    print(re)
