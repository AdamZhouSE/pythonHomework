class Solution(object):
    def small(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        parent = [i for i in range(len(s))]
        def find(v):
            if v == parent[v]:
                return v
            return find(parent[v])
        def union(v1,v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 > p2:
                parent[p1] = p2
            else:
                parent[p2] = p1
        
        for (i,j) in pairs:
            union(i,j)
        dic_val = {}
        for i in range(len(parent)):
            p = find(i)
            parent[i] = p
            dic_val[p] = dic_val.setdefault(p,'') + s[i]
        #print(parent)
        for key in dic_val.keys():
            dic_val[key] = ''.join(sorted(list(dic_val[key])))

        res = ''
        for i in parent:
            res += dic_val[i][0]
            dic_val[i] = dic_val[i][1:]

        return res
s=input()

pairs=input().lstrip('[[').rstrip(']]').split('],[')
p=[]
for i in pairs:
    x=i.split(',')
    for j in range(2):
        x[j]=int(x[j])
    p.append(x)

print(Solution().small(s,p))






















