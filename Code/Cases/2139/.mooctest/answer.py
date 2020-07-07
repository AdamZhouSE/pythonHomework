#include <bits/stdc++.h>
#define ll long long
#define Db double
#define GC() getchar()
#define For(x, y, z) for (int x = y; x <= z; x++)
#define Rep(x, y, z) for (int x = y; x >= z; x--)
using namespace std;
inline ll Getint() {
    char ch = GC();
    ll x = 0, fh = 1;
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            fh = -1;
        ch = GC();
    }
    while (ch >= '0' && ch <= '9') {
        (x *= 10) += ch ^ 48;
        ch = GC();
    }
    return x * fh;
}
const int N = 50005;
struct Starry {
    int next, to, id;
} h[N << 1];
int n, m, top = 1, g[N];
inline void Addside(int x, int y, int z) {
    h[++top] = (Starry){ g[x], y, z };
    g[x] = top;
    h[++top] = (Starry){ g[y], x, z };
    g[y] = top;
}
int f[N], son[N], sz[N], dep[N], si[N];
void Dfs1(int u, int fa) {
    f[u] = fa;
    sz[u] = 1;
    son[u] = 0;
    dep[u] = dep[fa] + 1;
    for (int i = g[u]; i; i = h[i].next) {
        int v = h[i].to;
        if (v == fa)
            continue;
        si[v] = h[i].id;
        Dfs1(v, u);
        sz[u] += sz[v];
        if (sz[son[u]] < sz[v])
            son[u] = v;
    }
}

int up[N], id[N], dfn[N], cnt;
void Dfs2(int u, int tp) {
    up[u] = tp;
    id[dfn[u] = ++cnt] = u;
    if (son[u])
        Dfs2(son[u], tp);
    for (int i = g[u]; i; i = h[i].next) {
        int v = h[i].to;
        if (v == f[u] || v == son[u])
            continue;
        Dfs2(v, v);
    }
}

int L[N << 2], R[N << 2], mi[N << 2];
int Ans[N << 2];
void Build(int v, int l, int r) {
    L[v] = l;
    R[v] = r;
    mi[v] = 1 << 30;
    int mid = l + r >> 1;
    if (l == r)
        return;
    Build(v << 1, l, mid);
    Build(v << 1 | 1, mid + 1, r);
}
void Ins(int v, int x, int y, int w) {
    if (x > R[v] || y < L[v])
        return;
    if (x <= L[v] && R[v] <= y) {
        mi[v] = min(mi[v], w);
        return;
    }
    Ins(v << 1, x, y, w);
    Ins(v << 1 | 1, x, y, w);
}
void Del(int v) {
    if (L[v] == R[v]) {
        Ans[si[id[L[v]]]] = mi[v];
        return;
    }
    mi[v << 1] = min(mi[v << 1], mi[v]);
    mi[v << 1 | 1] = min(mi[v << 1 | 1], mi[v]);
    Del(v << 1);
    Del(v << 1 | 1);
}
inline void Ins(int x, int y, int w) {
    while (up[x] != up[y]) {
        if (dep[up[x]] < dep[up[y]])
            swap(x, y);
        Ins(1, dfn[up[x]], dfn[x], w);
        x = f[up[x]];
    }
    if (x == y)
        return;
    if (dep[x] > dep[y])
        swap(x, y);
    Ins(1, dfn[son[x]], dfn[y], w);
}
int main() {
    int x, y, z;
    n = Getint();
    m = Getint();
    For(i, 1, n - 1) {
        x = Getint();
        y = Getint();
        Addside(x, y, i);
    }
    Dfs1(1, 0);
    Dfs2(1, 1);
    Build(1, 1, n);
    For(i, 1, m) {
        x = Getint();
        y = Getint();
        z = Getint();
        Ins(x, y, z);
    }
    Del(1);
    For(i, 1, n - 1) {
        if (Ans[i] == (1 << 30))
            puts("-1");
        else
            cout << Ans[i] << '\n';
    }
    return 0;
}