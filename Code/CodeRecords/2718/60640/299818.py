import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [int]) -> str:
        p = {i: i for i in range(len(s))}  # 初始化并查集
       
        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]

        for i, j in pairs:
            p[f(j)] = f(i)
            # 合并可交换位置
        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)
        # 排序
        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)
            for i, c in zip(sorted(q), t):
                ans[i] = c
        return ''.join(ans)


if __name__ == "__main__":
    inp = input()
    arr = eval(input())
    s = Solution()
    res = s.smallestStringWithSwaps(inp, arr)
    print(res)
