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
            re = re+s[i][0]
        
        return re


if __name__ == '__main__':
    s = input()
    s = Solution()
    re = s.find(s)
    print(re,end='')
