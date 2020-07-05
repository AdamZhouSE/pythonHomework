import collections
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

def search11():
    dsu=DSU()
    set=[]
    strs=input()[2:-2].split('], [')
    for i in range(len(strs)):
        items=strs[i][1:-1].split('", "')
        set.append(items)
    dic_name={}
    dic_id={}
    i=0
    for item in set:
        name=item[0]
        for email in item[1:]:
            dic_name[email]=name
            if(email not in dic_id):
                dic_id[email]=i
                i+=1
            dsu.union(dic_id[email],dic_id[item[1]])
    ans = collections.defaultdict(list)
    for email in dic_name:
        ans[dsu.find(dic_id[email])].append(email)

    print([[dic_name[v[0]]] + (v) for v in ans.values()])
    return



search11()