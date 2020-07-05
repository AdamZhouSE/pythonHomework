class Solution:
    def trans(self, n):
        re = ''
        while n!=0:
            s = n//-2
            r = n % -2
            if r==-1: # n满足>0
                s+=1
                r=1
            re = str(r)+re
            n = s
        return list(re)

    def find(self, a, b):
        xxx = 0
        for i in range(len(a)):
            xxx += a[i]* pow(-2,len(a)-1-i)
        yyy = 0
        for i in range(len(b)):
            yyy += b[i]* pow(-2, len(b)-1-i)
        n = xxx+yyy
        re = self.trans(n)
        res = []
        for i in re:
            res.append(int(i))
        return res

    ''' 
    #此路不通
    def find(self, a, b):
        if len(b) > len(a):
            tmp = a
            a = b
            b = tmp
        t1 = []
        t2 = []
        for i in range(len(a) - 1, -1, -1):
            t1.append(a[i])
        a = t1
        for i in range(len(b) - 1, -1, -1):
            t2.append(b[i])
        b = t2

        carry = 0
        for i in range(len(a)):
            if i<len(b):
                a[i] = a[i] + b[i] + carry
            else:
                a[i] = a[i] + carry
            carry = 0
            if a[i] == 2:
                if i!=len(a)-1:
                    a[i] = 0
                    a[i+1] -= 1
                else:
                    a.append(-1)
            elif a[i]==3:
                a[i]= 1
                a[i+1]-=1

        t3 = []
        for i in range(len(a) - 1, -1, -1):
            t3.append(a[i])
        return t3
    '''

if __name__ == '__main__':
    a = [int(x) for x in input().split(',')]
    b = [int(x) for x in input().split(',')]
    ss = Solution()
    re = ss.find(a, b)
    print(re)
