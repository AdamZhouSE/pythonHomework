class Solution:
    def fourSumCount(self,A, B, C, D):
        a=[]
        b=[]
        count=0
        for x in A:
            for y in B:
                a.append(x+y)
        for x in C:
            for y in D:
                b.append(x+y)
        for x in a:
            for y in b:
                if x+y==0:
                    count+=1
        return count
t=Solution()
a=input().split(',')
a=[int(x) for x in a]
b=input().split(',')
b=[int(x) for x in b]
c=input().split(',')
c=[int(x) for x in c]
d=input().split(',')
d=[int(x) for x in d]
print(t.fourSumCount(a,b,c,d))