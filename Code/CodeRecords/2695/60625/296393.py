#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>

#define int long long

inline void read(int & x)
{
    x = 0;
    int k = 1;
    char c = getchar();
    while (!isdigit(c))
        if (c == '-') c = getchar(), k = -1;
        else c = getchar();
    while (isdigit(c))
        x = (x << 1) + (x << 3) + (c ^ 48),
        c = getchar(); 
    x *= k;
}

struct edge
{
    int v;
    int u;
    int nxt;
}e[201020];

int n, m, x, y, z, cnt, nid, opt;

int f[102020];
int siz[102020];
int faz[102020];
int dep[102020];
int son[102020];
int tid[102020];
int tva[102020];
int top[102020];
int val[102020];

void addedge(int x, int y)
{
    ++cnt;
    e[cnt].u = x;
    e[cnt].v = y;
    e[cnt].nxt = f[x];
    f[x] = cnt;
}

//first operation

void dfs0(int u, int father, int deep)
{
    faz[u] = father;
    dep[u] = deep;
    siz[u] = 1;
    for (int i = f[u]; i != -1; i = e[i].nxt)
    {
        if (e[i].v == father) continue;
        dfs0(e[i].v, u, deep + 1);
        siz[u] += siz[e[i].v];
        if (son[u] == -1 || siz[son[u]] < siz[e[i].v]) 
            son[u] = e[i].v;
    }
}

void dfs1(int u, int head)
{
    ++nid;
    tid[u] = nid;
    tva[nid] = val[u];
    top[u] = head;
    
    if (son[u] == -1) return;
    
    dfs1(son[u], head);
    
    for (int i = f[u]; i != -1; i = e[i].nxt)
        if (!tid[e[i].v]) dfs1(e[i].v, e[i].v);
}

//segment tree

#define root 1, 1, n
#define lson u << 1, l, mid
#define rson u << 1 | 1, mid + 1, r
#define ls u << 1
#define rs u << 1 | 1

struct tree
{
    int l;
    int r;
    int w;
    int f;
}t[402020];

void update(int u) 
{
    t[u].w = t[ls].w + t[rs].w; 
}

void build(int u, int l, int r)
{
    t[u].l = l, t[u].r = r;
    if (l == r)
    {
        t[u].w = tva[l];
        return; 
    }
    int mid = (l + r) >> 1;
    build(lson);
    build(rson);
    update(u); 
}

void pushdown(int u)
{
    if (!t[u].f) return;
    t[ls].w += (t[ls].r - t[ls].l + 1) * t[u].f;
    t[rs].w += (t[rs].r - t[rs].l + 1) * t[u].f;
    t[ls].f += t[u].f;
    t[rs].f += t[u].f;
    t[u].f = 0;
}

void add(int u, int l, int r, int c, int x, int y)
{
    if (l >= x && r <= y) 
    {
        t[u].w += (t[u].r - t[u].l + 1) * c;
        t[u].f += c;
        return;
    }
    pushdown(u);
    int mid = (l + r) >> 1;
    if (y > mid) add(rson, c, x, y);
    if (x <= mid) add(lson, c, x, y);
    update(u);
}

int query(int u, int l, int r, int x, int y)
{
    int ans_in_tree = 0;
    if (l >= x && r <= y) return t[u].w;
    pushdown(u);
    int mid = (l + r) >> 1;
    if (y > mid) ans_in_tree += query(rson, x, y);
    if (x <= mid) ans_in_tree += query(lson, x, y);
    return ans_in_tree;
}

//break the tree

void tsum(int x, int y)
{
    int ans = 0;
    while (top[x] != top[y])
    {
        if (dep[top[x]] < dep[top[y]]) x ^= y, y ^= x, x ^= y;
        ans += query(root, tid[top[x]], tid[x]);
        x = faz[top[x]];
    }
    if (dep[x] > dep[y]) x ^= y, y ^= x, x ^= y;
    ans += query(root, tid[x], tid[y]);
    printf("%lld\n", ans);
}
#undef int

int main()
{
    #define int long long
    memset(f, -1, sizeof(f));
    memset(son, -1, sizeof(son));
    read(n), read(m);
    for (int i = 1; i <= n; ++i) read(val[i]);
    for (int i = 1; i < n; ++i)
    {
        read(x), read(y);
        addedge(x, y);
        addedge(y, x);
    }
    dfs0(1, 0, 1);
    dfs1(1, 1);
    build(root);
    for (int i = 1; i <= m; ++i)
    {
        read(opt), read(x);
        if (opt == 1)
        {
            read(z);
            add(root, z, tid[x], tid[x]);
        }
        else if (opt == 2)
        {
            read(z);
            add(root, z, tid[x], tid[x] + siz[x] - 1);
        }
        else if (opt == 3)
            tsum(1, x);
    }
}