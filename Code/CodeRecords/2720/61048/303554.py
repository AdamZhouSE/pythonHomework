
class DSU:
    def __init__(self):
        self.par = [int(x) for x in range(10001)]

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def same(self, x, y):
        return self.find(x) == self.find(y)

def search15():
    dsu=DSU()
    set=[]
    num=int(input())
    strs=input()[2:-2].split('],[')
    for i in range(len(strs)):
        items=strs[i].split(',')
        set.append([int(x) for x in items])
    cnt=len(set)

    for link in set:
        x1=dsu.find(link[0])
        x2 = dsu.find(link[1])
        if(x1!=x2):
            dsu.union(link[0],link[1])
            cnt-=1
    '''for i in range(num):
        for j in range(num):
            if(i!=j and dsu.find(i)==dsu.find(j)):
                cnt-=1'''
    if(len(set)>=num-1):
        print(cnt)
    else:print(-1)
    return

search15()