#include <bits/stdc++.h>
#define id(x, y) ((x) * (k + 1) + y)

using namespace std;

const int N = 4e4 + 5;
const int M = 6e7 + 5;
inline void chkmx(int& a, int b) {
    if (a < b)
        a = b;
}
int _w;

int n, k, mark[N], f[M], g[M], dfn1[N], dfn2[N], siz[N], rmp1[N], rmp2[N], dfc1, dfc2, a[N], v[N], val[N],
    ans;
vector<int> G[N];

void clr(void) {
    dfc1 = dfc2 = 0;
    for (int i = 1; i <= n; ++i) {
        vector<int> vec;
        swap(vec, G[i]);
        mark[i] = 0;
    }
}

int que[M], he, ta;

void dfs1(int u) {
    siz[u] = 1, val[u] += v[u];
    for (const int& v : G[u]) val[v] = val[u], dfs1(v), siz[u] += siz[v];
    rmp1[dfn1[u] = ++dfc1] = u;
}

void dfs2(int u) {
    reverse(G[u].begin(), G[u].end());
    for (const int& v : G[u]) dfs2(v);
    rmp2[dfn2[u] = ++dfc2] = u;
}

void dp(int* f, int* rmp) {
    for (int i = 0; i <= k; ++i) f[i] = 0;
    for (int i = 1, c, v, sz; i <= n; ++i) {
        c = a[rmp[i]], sz = siz[rmp[i]], v = ::v[rmp[i]];
        que[he = ta = 1] = 0, f[id(i, 0)] = 0;
        for (int j = 1; j <= k; ++j) {
            f[id(i, j)] = f[id(i - sz, j)];
            while (he <= ta && j - que[he] > c) ++he;
            chkmx(f[id(i, j)], f[id(i - 1, que[he])] + (j - que[he]) * v);
            while (he <= ta && f[id(i - 1, j)] - j * v > f[id(i - 1, que[ta])] - que[ta] * v) --ta;
            que[++ta] = j;
        }
    }
}

void solve(void) {
    _w = scanf("%d%d", &n, &k);
    for (int i = 1, x; i <= n; ++i) {
        _w = scanf("%d%d%d", &x, a + i, v + i);
        if (x)
            mark[x] = 1, G[x].push_back(i);
    }
    for (int i = n; i; --i)
        if (a[i] > 1) {
            a[++n] = a[i] - 1;
            a[i] = 1;
            v[n] = v[i];
            G[i].push_back(n);
            mark[n] = 1;
        }
    ans = 0;
    val[1] = 0;
    dfs1(1), dfs2(1);
    dp(f, rmp1);
    dp(g, rmp2);
    for (int i = 1; i <= n; ++i)
        if (!mark[i])
            for (int j = 0; j <= k; ++j)
                chkmx(ans, val[i] + f[id(dfn1[i] - 1, j)] + g[id(dfn2[i] - siz[i], k - j)]);
    printf("%d\n", ans);
    clr();
}

int main(void) {
    int T;
    _w = scanf("%d", &T);
    while (T--) solve();
    return 0;
}