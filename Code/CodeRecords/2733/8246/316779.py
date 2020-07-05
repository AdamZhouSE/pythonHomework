#include<bits/stdc++.h>
using namespace std;
#define id(u) (lower_bound(b + 1, b + 1 + tot, a[u]) - b)

const int maxn = 1e6 + 1;

inline int read()
{
    register int x = 0, ch = getchar(), f = 1;
    while(!isdigit(ch)) {if(ch == '-') f = -1; ch = getchar();}
    while(isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
    return x * f;
}

int n, tot, m;

int a[maxn], b[maxn];

struct tree{
    int l, r;
    int sum;
}t[maxn];

struct node{
    int ne;
    int to;
}e[maxn << 1];

int cnt, head[maxn];

int dep[maxn], fa[maxn][21], rt[maxn];

void add(int x, int y)
{
    e[++  cnt].to = y;
    e[cnt].ne = head[x];
    head[x] = cnt;
}

void dfs(int u, int d)
{
    dep[u] = d;
    for(int i = 1; i <= 19; i ++)
    {
        fa[u][i] = fa[fa[u][i - 1]][i - 1];
    }
    for(int i = head[u]; i; i = e[i].ne)
    {
        int v = e[i].to;
        if(v == fa[u][0]) continue;
        fa[v][0] = u;
        dfs(v, d + 1);
    }
}

int add(int pre, int l, int r, int x)
{
    int p = ++ cnt;
    t[p] = t[pre];
    t[p].sum ++;
    int mid = l + r >> 1;
    if(l < r)
    {
        if(x <= mid) t[p].l = add(t[pre].l, l, mid, x);
        else t[p].r = add(t[pre].r , mid + 1, r, x);
    }
    return p;
}

void dfs2(int u)
{
    rt[u] = add(rt[fa[u][0]], 1, tot, id(u));
    for(int i = head[u]; i; i = e[i].ne)
    {
        int v = e[i].to;
        if(v == fa[u][0]) continue;
        dfs2(v);
    }
}

int LCA(int u, int v)
{
    if(dep[u] > dep[v]) std:: swap(u, v);
    for(int d = dep[v] - dep[u], i = 0; d; d >>= 1, i ++)
    {
        if(d & 1) v = fa[v][i];
    }
    if(u == v) return u;
    for(int i = 19; i >= 0; i --)
    {
        if(fa[u][i] != fa[v][i])
        {
            u = fa[u][i];
            v = fa[v][i];
        }
    }
    return fa[u][0];
}

int query(int x, int y, int z, int w, int l, int r, int k)
{
    if(l == r) return l;
    int sum = t[t[x].l].sum + t[t[y].l].sum - t[t[z].l].sum - t[t[w].l].sum;
    int mid = l + r >> 1;
    if(sum >= k ) return query(t[x].l, t[y].l, t[z].l, t[w].l, l, mid, k);
    else return query(t[x].r, t[y].r, t[z].r, t[w].r, mid + 1, r, k - sum);
}

int main()
{
    n = read();
    m = read();
    for(int i = 1; i <= n; i ++) a[i] = read(), b[i] = a[i];
    for(int i = 1; i < n; i ++)
    {
        int x = read(), y = read();
        add(x, y), add(y, x);
    }
    std:: sort(b + 1, b + 1 + n);
    tot = unique(b + 1, b + 1 + n) - b - 1;
    dfs(1, 0);
    dfs2(1);
    int lastans = 0;
    while(m --)
    {
        int x = read() ^ lastans;
        int y = read();
        int k = read();
        int z = LCA(x, y);
        lastans = b[query(rt[x], rt[y], rt[z], rt[fa[z][0]], 1, tot, k)];
        printf("%d\n", lastans);
    }
}