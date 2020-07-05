class Solution:
    def find(self, data):
        n = len(data)
        tmp = data
        s = []
        for i in range(n):
            tmp = tmp[1:n+1]+tmp[0]
            s.append(tmp)
        s.sort()
        re = ''
        for i in range(n):
            re = re+s[i][n-1]
        return re


if __name__ == '__main__':
    s = input()
    ss = Solution()
    re = ss.find(s)
    print(re,end='')
