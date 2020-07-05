import collections

class Function:
    def find(self, n, edges):
        if n == 0: return []
        g = collections.defaultdict(set)
        for i, j in edges: g[i].add(j), g[j].add(i)
        t = dict()
        def func(s, k):
            if (s, k) not in t:
                c = [func(k, e) for e in g[k] if s != e]
                t[s, k] = max(c) + 1 if c else 1
            return t[s, k]
        a = [func(None, i) for i in range(n)]
        m = min(a)
        a = [i for i, c in enumerate(a) if c == m]
        return a

s1=int(input())
s2=eval(input())
s=Function()
res=s.find(s1,s2)
print(res)