class Solution:
    def find(self, a, b):
        if len(b)>len(a):
            tmp = a
            a=b
            b=tmp
        t1 = []
        t2=[]
        for i in range(len(a)-1,-1,-1):
            t1.append(a[i])
        a = t1
        for i in range(len(b)-1,-1,-1):
            t2.append(b[i])
        b = t2
        for i in range(len(b)):
            if b[i]==0:
                continue
            else:
                if a[i]==0:
                    a[i]==1
                else:
                    a[i+1]-=1
        t3 = []
        for i in range(len(a)-1,-1,-1):
            t3.append(a[i])
        return t3
    


if __name__ == '__main__':
    a = [int(x) for x in input().split(',')]
    b = [int(x) for x in input().split(',')]
    s = Solution()
    re = s.find(a,b)
    print(re)
