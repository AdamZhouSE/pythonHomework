class Solution :
    def powerof2(self):
        n = int(input())
        lis = []
        while n > 0:
            remainer = n % 10
            lis.append(remainer)
            n = int(n / 10)
        lis.sort()
        if n < 10 :
            if lis==[1] or lis==[2] or lis==[4] or lis==[8] :
                return 'true'
            else:
                return 'false'
        if n < 100 :
            if lis==[1,6] or lis==[2,3] or lis==[4,6] :
                return 'true'
            else:
                return 'false'
        if n < 1000 :
            if lis==[1,2,8] or lis==[2,5,6] or lis==[1,2,5] :
                return 'true'
            else:
                return 'false'
        if n < 10000 :
            if lis==[0,1,2,4] or lis==[0,2,4,8] or lis==[0,4,6,9] or lis==[1,2,8,9] :
                return 'true'
            else:
                return 'false'
        return 'false'
so = Solution()
print(so.powerof2())