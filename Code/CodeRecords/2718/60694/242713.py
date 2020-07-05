from collections import defaultdict

def smallestStringWithSwaps(s: str, pairs: [[int]]) -> str:
    parent = list(range(len(s)))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(v1, v2):
        r1 = find(v1)
        r2 = find(v2)
        parent[r1] = r2

    for i, j in pairs:
        union(i, j)

    dic = defaultdict(list)

    for i, k in enumerate(parent):
        dic[find(k)].append(s[i])
    for k in dic:
        dic[k].sort()

    result = []
    for i in range(len(s)):
        result.append(dic[find(i)][0])
        del dic[find(i)][0]
    return "".join(result)


str = input()
pairs = eval(input())
print(smallestStringWithSwaps(str, pairs))
