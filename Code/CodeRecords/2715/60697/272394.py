# class DSU:
#     def __init__(self, N):
#         self.p = range(N)
#
#     def find(self, x):
#         if self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#
#     def union(self, x, y):
#         xr = self.find(x)
#         yr = self.find(y)
#         self.p[xr] = yr
#
# class Solution(object):
#     def removeStones(self, stones):
#         N = len(stones)
#         dsu = DSU(20000)
#         for x, y in stones:
#             dsu.union(x, y + 10000)
#
#         return N - len({dsu.find(x) for x, y in stones})
stones=eval(input())
p=[i for i in range(20000)]
def union(x,y):
    p[find(x)]=find(y)
def find(x):
    if(x!=p[x]):
        x=find(p[x])
    return x
leng=len(stones)
tmp={}
for i in range(leng):
    union(stones[i][0],stones[i][1]+10000)
for i in range(leng):
    x=find(stones[i][0])
    tmp.setdefault(x,0)
    tmp[x]+=1
print(leng-len(tmp))

