class UnionFind():
    def __init__(self):
        self.father=list(range(10001))
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
import collections
accounts=eval(input())
uf=UnionFind()
emtoname,emtoid,i={},{},0
for account in accounts:
    name=account[0]
    for email in account[1::]:
        emtoname[email]=name
        if email not in emtoid:
            emtoid[email]=i
            i+=1
        uf.union(emtoid[account[1]],emtoid[email])#每个账户以首个邮箱作为父节点
    ansemails=collections.defaultdict(list)
for email in emtoname:
    ansemails[uf.find(emtoid[email])].append(email)
ans=[]
for value in ansemails.values():
    ans.append([emtoname[value[0]]]+value)
print(ans)


