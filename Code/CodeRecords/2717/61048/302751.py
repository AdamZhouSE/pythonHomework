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

def search13():
    strs=input()[2:-2].split('","')
    '''parent=[int(x) for x in range(256)]'''
    dsu=DSU()
    res='true'
    for i in range(len(strs)):
        if(strs[i][1]=='='):
            x1=dsu.find(ord(strs[i][0]))
            x2=dsu.find(ord(strs[i][3]))
            if(x1!=x2):
                dsu.union(ord(strs[i][0]),ord(strs[i][3]))
    for i in range(len(strs)):
        if(strs[i][1]=='!'):
            x1 = dsu.find(ord(strs[i][0]))
            x2 = dsu.find(ord(strs[i][3]))
            if (x1 == x2):
                res='false'
                break
    print(res)
    return


search13()