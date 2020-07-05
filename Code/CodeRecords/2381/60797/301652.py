class Solution:
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
            if i!= len(a)-1 and a[i] == 2:
                a[i] = 0
                a[i+1] -= 1

            elif a[i]==3:
                a[i]= 1
                a[i+1]-=1

        t3 = []
        for i in range(len(a) - 1, -1, -1):
            t3.append(a[i])
        return t3


if __name__ == '__main__':
    a = [int(x) for x in input().split(',')]
    b = [int(x) for x in input().split(',')]
    s = Solution()
    re = s.find(a, b)
    print(re)
