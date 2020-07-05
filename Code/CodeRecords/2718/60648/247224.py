import collections
class Solution:
    def smallestStringWithSwaps(self, s, pairs) -> str:
        single_pairs = set()
        for i in pairs:
            single_pairs.add(i[0])
            single_pairs.add(i[1])
        self.parent = [-1 if i in single_pairs else -2 for i in range(len(s))]
        self.rank = [1 for _ in self.parent]

        def find(x):
            if self.parent[x] == -1:
                return x
            else:
                return find(self.parent[x])
        

        def union(i, j):
            iroot = find(i)
            jroot = find(j)
            if iroot != jroot:
                if self.rank[iroot] > self.rank[jroot]:
                    self.parent[jroot] = iroot
                elif self.rank[iroot] < self.rank[jroot]:
                    self.parent[iroot] = jroot
                else:
                    self.parent[jroot] = iroot
                    self.rank[iroot] += 1


        def union_find(s):
            for i in pairs:
                union(i[0], i[1])
            # print(self.parent)
            
            res = {}

            for i in range(len(s)):
                if self.parent[i] != -2:
                    res.setdefault(find(i), []).append(i)
            # print(res)

            s = list(s)
            for i in res:
                to_sort = [s[j] for j in res[i]]
                temp = sorted(to_sort)
                # print(temp)
                for m in res[i]:
                    s[m] = temp.pop(0)
            return ''.join(s)

        return union_find(s)


if __name__=="__main__":
    #ls=[]
    s=input()
    pairs=input().strip('[]').split('],[')
    pairs=[i.split(",") for i in pairs]
    for i in range(len(pairs)):
        for j in range(2):
            pairs[i][j]=int(pairs[i][j])
    print(pairs)
    x=Solution().smallestStringWithSwaps(s,pairs)
    print(x)
    