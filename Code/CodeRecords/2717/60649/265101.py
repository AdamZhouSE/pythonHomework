class UnionFind():
    def __init__(self,n):
        self.father=list(range(n))
    def find(self,x):
        f=x
        while f!=self.father[f]:
            f=self.father[f]
        while f!=x:
            x,self.father[x]=self.father[x],f
        return f
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px!=py:
            self.father[py]=px
equations=eval(input())
uf=UnionFind(26)
for equation in equations:
    if equation[1]=='=':
        x=ord(equation[0])-ord('a')
        y=ord(equation[3])-ord('a')
        uf.union(x,y)
for equation in equations:
    if equation[1]=='!':
        x = ord(equation[0]) - ord('a')
        y = ord(equation[3]) - ord('a')
        if uf.find(x)==uf.find(y):
            print("false")
            break
else:
    print("true")