class Solution(object):
    def fourSumCount(self, A, B, C, D):
        dic={}
        for a in A:
            for b in B:
                if -a-b in dic:
                    dic[-a-b] += 1
                else:
                    dic[-a-b] = 1
        return sum(dic[c+d] for c in C for d in D if c+d in dic)
t=Solution()
a=input().split(',')
a=[int(x) for x in a]
b=input().split(',')
b=[int(x) for x in a]
c=input().split(',')
c=[int(x) for x in a]
d=input().split(',')
d=[int(x) for x in a]
print(t.fourSumCount(a,b,c,d))
