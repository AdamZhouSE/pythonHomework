class Solution:
    def find(self, a, b):
        if len(b)>len(a):
            tmp = a
            a=b
            b=tmp
        a = a.reverse()
        b = b.reverse()
        for i in range(len(b)):
            if b[i]==0:
                continue
            else:
                if a[i]==0:
                    a[i]==1
                else:
                    a[i+1]-=1
        a = a.reverse()
        return a


if __name__ == '__main__':
    a = [int(x) for x in input().split(',')]
    b = [int(x) for x in input().split(',')]
    s = Solution()
    re = s.find(a,b)
    print(re)
