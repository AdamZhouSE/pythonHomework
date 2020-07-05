class Solution:
    def find(self, n, h, a):
        re = 0
        for i in range(n):
            if a[i]<h:
                re +=1
            else:
                re +=2
        return re

if __name__ == '__main__':
    tmp = input().split()
    n = int(tmp[0])
    h = int(tmp[1])
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, h, data)
    print(re)
