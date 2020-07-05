def bb(m):
    
    uf={}
    def find(x):
        if x!=uf[x]:
            uf[x]=find(uf[x])
        return uf[x]
    def union(x,y):
        uf.setdefault(x,x)
        uf.setdefault(y,y)
        uf[find(x)]=find(y)
    for i,j in m:
        union(i,~j)
    print(len(m)-len({find(x) for x in uf}))
if __name__ == '__main__':
    bb(eval(input()))
