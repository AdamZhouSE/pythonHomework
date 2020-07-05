import collections
class UF:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while x != self.parent[x]:
            x = self.parent[x]
        return x 
    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)


class Solution:
    def accountsMerge(self, accounts):
        uf = UF()
        email_to_name = {}
        res = collections.defaultdict(list)
        for account in accounts:
            for i in range(1, len(account)):
                email_to_name[account[i]] = account[0]
                if i < len(account) - 1:uf.union(account[i], account[i + 1])
        for email in email_to_name:
            res[uf.find(email)].append(email)
        
        return [[email_to_name[value[0]]] + sorted(value) for value in res.values()]

    
if __name__=="__main__":
    stones=input().strip('[]').strip('"').split('"], ["')
    #print(stones)
    stones=[i.split('", "') for i in stones]
    l=len(stones)
    #print(stones)
    '''
    for i in range(l):
        for j in range(len(stones[0])):
            stones[i][j]=int(stones[i][j])
            '''
    x=Solution().accountsMerge(stones)
    print(x)