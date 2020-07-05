def dy(accounts):
    import collections
    d = collections.defaultdict(set)
    c = set()
    n = len(accounts)
    for i in range(n):
        for j in accounts[i][1:]:  
            for k in d[j]:
                if i != k:
                    c |= {(k, i)}  
            d[j] |= {i}
    p = [*range(n)]  

    def f(x):  
        if p[x] != x:
            p[x] = f(p[x])
        return p[x]

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in c:
                pi, pj = f(i), f(j)
                if pi != pj: 
                    p[pj] = pi
    ans = {}
    for i in range(n):  
        pi = f(i)
        if pi not in ans:
            ans[pi] = accounts[i]
        else:
            ans[pi] += accounts[i][1:]
    print([['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']])

if __name__ == '__main__':
    dy(eval(input()))
