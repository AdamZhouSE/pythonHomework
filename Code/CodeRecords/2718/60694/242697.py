from collections import defaultdict

def smallestStringWithSwaps(s: str, pairs: [[int]]) -> str:
    p = list(range(len(s)))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(v1, v2):
        r1 = find(v1)
        r2 = find(v2)
        p[r1] = r2

    for i, j in pairs:
        union(i, j)

    dic = defaultdict(list)

    for i, v in enumerate(p):
        dic[find(v)].append(s[i])
    for k in dic:
        dic[k].sort()

    res = []
    for i in range(len(s)):
        res.append(dic[find(i)][0])
        del dic[find(i)][0]
    return "".join(res)


str = input()
pairs = eval(input())
print(smallestStringWithSwaps(str, pairs))
