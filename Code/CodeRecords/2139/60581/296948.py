#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
using namespace std;
#define reg register
inline int read() {
    int res = 0;char ch=getchar();bool fu=0;
    while(!isdigit(ch))fu|=(ch=='-'),ch=getchar();
    while(isdigit(ch)) res=(res<<3)+(res<<1)+(ch^48),ch=getchar();
    return fu?-res:res;
}
#define N 50005
int n, m;
struct edge {
    int nxt, to, from, id;
}ed[N<<1];
int head[N], cnt;
inline void add(int x, int y, int id) {
    ed[++cnt] = (edge){head[x], y, x, id};
    head[x] = cnt;
}
struct date {
    int x, y, val;
    inline bool operator < (const date &a) const {
        return val > a.val;
    }
}da[N];
int ans[N];

int Fa[N], top[N], id[N], rnk[N], dep[N], siz[N], son[N], tot;

void dfs1(int x, int fa)
{
    Fa[x] = fa, dep[x] = dep[fa] + 1, siz[x] = 1;
    for (reg int i = head[x] ; i ; i = ed[i].nxt)
    {
        int to = ed[i].to;
        if (to == fa) continue;
        dfs1(to, x);
        siz[x] += siz[to];
        if (siz[to] > siz[son[x]]) son[x] = to;
    }
}

void dfs2(int x, int tep)
{
    id[x] = ++tot, rnk[tot] = x;
    top[x] = tep;
    if (son[x]) dfs2(son[x], tep);
    for (reg int i = head[x] ; i ; i = ed[i].nxt)
    {
        int to = ed[i].to;
        if (to == Fa[x] or to == son[x]) continue;
        dfs2(to, to);
    }
}

int tr[N << 2], lzy[N << 2];
#define ls o << 1
#define rs o << 1 | 1
inline void pushup(int o) {
    tr[o] = tr[ls] + tr[rs];
}
inline void spread(int o, int l, int r)
{
    if (!lzy[o]) return;
    lzy[ls] = lzy[rs] = lzy[o];
    int mid = (l + r) >> 1;
    tr[ls] = lzy[o] * (mid - l + 1);
    tr[rs] = lzy[o] * (r - mid);
    lzy[o] = 0;
}
void change(int l, int r, int o, int ql, int qr, int c)
{
    if (l >= ql and r <= qr) {
        tr[o] = (r - l + 1) * c;
        lzy[o] = c;
        return ;
    }
    spread(o, l, r);
    int mid = (l + r) >> 1;
    if (ql <= mid) change(l, mid, ls, ql, qr, c);
    if (qr > mid) change(mid + 1, r, rs, ql, qr, c);
    pushup(o);
}
void changes(int x, int y, int c)
{
    while(top[x] != top[y]) 
    {
        if (dep[top[x]] < dep[top[y]]) swap(x, y);
        change(1, n, 1, id[top[x]], id[x], c);
        x = Fa[top[x]];
    }
    if (id[x] > id[y]) swap(x, y);
    change(1, n, 1, id[x] + 1, id[y], c);
}
int query(int l, int r, int o, int p)
{
//    printf("%d %d %d\n", l, r, tr[o]);
    if (l == r) return tr[o];
    spread(o, l, r);
    int mid = (l + r) >> 1;
    if (p <= mid) return query(l, mid, ls, p);
    else return query(mid + 1, r, rs, p);
}

int main()
{
    n = read(), m = read();
    for (reg int i = 1 ; i < n ; i ++)
    {
        int x = read(), y = read();
        add(x, y, i), add(y, x, i);
    }
    for (reg int i = 1 ; i <= m ; i ++) da[i] = (date){read(), read(), read()};
    sort(da + 1, da + 1 + m);
    dfs1(1, 0);
    dfs2(1, 1);
//    for (int i=1;i<=n;i++) printf("siz[%d]=%d\n", i, siz[i]);
    for (reg int i = 1 ; i <= m ; i ++)
        changes(da[i].x, da[i].y, da[i].val);
    for (reg int i = 1 ; i <= cnt ; i += 2)
    {
        int x = ed[i].from, y = ed[i].to;
        if (dep[x] < dep[y]) swap(x, y);
        ans[ed[i].id] = query(1, n, 1, id[x]);
//        printf("%d\n",x);
    }
    for (reg int i = 1 ; i < n ; i ++) printf("%d\n", ans[i] > 0 ? ans[i] : -1);
    return 0;
}