#并查集
import collections


def smallestStringWithSwaps(s: str, pairs: [int]):
    p = {i: i for i in range(len(s))}  # 初始化并查集

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    for i, j in pairs:
        p[find(j)] = find(i)
        # 合并可交换位置
    d = collections.defaultdict(list)
    for i, j in enumerate(map(find, p)):
        d[j].append(i)
    # 排序
    ans = list(s)
    for q in d.values():
        t = sorted(ans[i] for i in q) # 只对一个集合中的元素排序
        for i, c in zip(sorted(q), t):
            ans[i] = c
    return ''.join(ans)

s = input()
pairs = eval(input())
print(smallestStringWithSwaps(s,pairs))