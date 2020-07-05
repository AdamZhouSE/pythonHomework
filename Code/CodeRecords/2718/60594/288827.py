def smallestStringWithSwaps(s: str, pairs) -> str:
    single_pairs = set()
    for i in pairs:
        single_pairs.add(i[0])
        single_pairs.add(i[1])
    parent = [-1 if i in single_pairs else -2 for i in range(len(s))]
    rank = [1 for _ in parent]
    def find(x):
        if parent[x] == -1:
            return x
        else:
            return find(parent[x])
    def union(i, j):
        iroot = find(i)
        jroot = find(j)
        if iroot != jroot:
            if rank[iroot] > rank[jroot]:
                parent[jroot] = iroot
            elif rank[iroot] < rank[jroot]:
                parent[iroot] = jroot
            else:
                parent[jroot] = iroot
                rank[iroot] += 1
    def union_find(s):
        for i in pairs:
            union(i[0], i[1])
        res = {}
        for i in range(len(s)):
            if parent[i] != -2:
                res.setdefault(find(i), []).append(i)
        s = list(s)
        for i in res:
            to_sort = [s[j] for j in res[i]]
            temp = sorted(to_sort)
            for m in res[i]:
                s[m] = temp.pop(0)
        return ''.join(s)
    return union_find(s)
s=input()
num=eval(input())
print(smallestStringWithSwaps(s,num))

