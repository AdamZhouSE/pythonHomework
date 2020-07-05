def search12():
    arr=input()[2:-2].split('","')
    dsu=DSU()
    res=len(arr)
    parent=[int(x) for x in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and isSimilar(arr[i],arr[j]):
                if(dsu.find(parent[i])!=dsu.find(parent[j])):
                    dsu.union(parent[i],parent[j])
                    res-=1
    print(res)

    return


def isSimilar(str1,str2):
    cnt=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            cnt+=1
    return True if cnt==0 or cnt==2 else False

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

search12()