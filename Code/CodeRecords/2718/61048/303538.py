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


def search14():
    str=input()
    res=[x for x in str]
    dsu=DSU()
    set=sorted(input()[2:-2].split('],['))
    for item in set:
        x1=dsu.find(int(item[0]))
        x2=dsu.find(int(item[2]))
        if(x1!=x2):
            dsu.union(int(item[0]),int(item[2]))
    for i in range(len(str)):
        tmp=[i]
        for j in range(len(str)):
            if(dsu.find(j)==i):
                tmp.append(j)
        for h in tmp:
            for k in tmp:
                if(h!=k and res[h]<res[k]):
                    res[h],res[k]=res[k],res[h]
    print(''.join(res))
    return

search14()