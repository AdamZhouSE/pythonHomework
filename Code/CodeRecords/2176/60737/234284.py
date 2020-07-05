def build_sa(s, n, m, c, sa, x, y):
    for i in range(0, n):
        x[i] = s[i]
        c[ord(x[i])] += 1
    for i in range(1, m):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        c[ord(x[i])] -= 1
        sa[c[ord(x[i])]] = i
    k = 1
    while k <= n:
        p = 0
        for i in range(n - k, n):
            y[p] = i
            p += 1
        for i in range(0, n):
            if sa[i] >= k:
                y[p] = sa[i] - k
                p += 1
        for i in range(0, m):
            c[i] = 0
        if k == 1:
            for i in range(0, n):
                c[ord(x[y[i]])] += 1
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[ord(x[y[i]])] -= 1
                sa[c[ord(x[y[i]])]] = y[i]
        else:
            for i in range(0, n):
                c[x[y[i]]] += 1
            for i in range(1, m):
                c[i] += c[i - 1]
            for i in range(n - 1, -1, -1):
                c[x[y[i]]] -= 1
                sa[c[x[y[i]]]] = y[i]
        x, y = y, x
        p = 1
        x[sa[0]] = 0
        for i in range(1, n):
            if y[sa[i - 1]] == y[sa[i]] and y[sa[i - 1] + k] == y[sa[i] + k]:
                x[sa[i]] = p - 1
            else:
                x[sa[i]] = p
                p += 1
        if p >= n:
            break
        m = p
        k = k * 2
    return


def get_suffix(s):
    m = 128
    n = len(s)
    maxn = 1000
    c = [0] * maxn
    sa = [0] * maxn
    x = [0] * maxn
    y = [0] * maxn
    suffix = [""] * n
    build_sa(s, n, m, c, sa, x, y)
    for i in range(0, n):
        suffix[i] = s[sa[i]:]
    return suffix


def get_rank(s, suffix):
    n = len(s)+1
    rank = []
    for i in range(0, n-1):
        rank.append(n - len(suffix[i]))
    return rank


if __name__ == "__main__":
    s = input()
    suffix = get_suffix(s)
    rank = get_rank(s, suffix)
    for i in range(0, len(s)-1):
        print(rank[i], end=' ')
    print(rank[len(s)-1])
