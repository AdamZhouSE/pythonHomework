class Solution:
    def find(self, n, t, c, data):
        re = 0
        p = 0
        count = 0
        #q = p + c - 1
        for i in range(n):
            if data[i]<=t:
                count += 1
                if count>=3:
                    re += 1
            else:
                count = 0
        return re


if __name__ == '__main__':
    [n, t, c] = [int(a) for a in input().split()]
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, t, c, data)
    print(re)
    if re==0:
        print(n,t,c)
        print(data)