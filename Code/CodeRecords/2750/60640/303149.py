import collections


class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 0:
            return []
        g = collections.defaultdict(set)
        for i, j in edges:
            g[i].add(j), g[j].add(i)
        t = dict()

        def func(s, k): # 以s为父结点时，k的高度
            if (s, k) not in t:
                c = [func(k, e) for e in g[k] if s != e]
                t[s, k] = max(c) + 1 if c else 1
            return t[s, k]
        a = [func(None, i) for i in range(n)]
        m = min(a)
        a = [i for i, c in enumerate(a) if c == m]
        return a


if __name__ == "__main__":
    N = int(input())
    E = eval(input())
    s = Solution()
    print(s.findMinHeightTrees(N, E))

