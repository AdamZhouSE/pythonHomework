class Solution:
    def find(self, n, data):
        re = 'YES'
        for i in range(n):
            for j in range(n):
                tmp = 0
                if i!=0:
                    if data[i-1][j]=='o':
                        tmp += 1
                if j!=0:
                    if data[i][j-1]=='o':
                        tmp += 1
                if j!=n-1:
                    if data[i][j+1]=='o':
                        tmp += 1
                if i!=n-1:
                    if data[i+1][j]=='o':
                        tmp += 1
                if tmp%2!=0:
                    re = 'NO'
        return re


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        line = input().split()
        data.append(line)
    s = Solution()
    re = s.find(n, data)
    print(re)
