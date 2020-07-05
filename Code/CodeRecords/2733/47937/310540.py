#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5 +7;
typedef long long ll;
int head[maxn], to[maxn<<1], nex[maxn<<1], tot, m, n, TT;
int val[maxn];
int tsize;
struct node {
    int l, r, sum;
}T[maxn * 20];
int v[maxn], root[maxn];
int getid(int x) {
    return lower_bound(v + 1, v + 1 + tsize, x) - v;
}
void add(int x, int y) {
    to[tot] = y;
    nex[tot] = head[x];
    head[x] = tot++;
}
int h[maxn], f[maxn][30];
void dfs(int x, int fx) {
    h[x] = h[fx] + 1;
    f[x][0] = fx;
    for (int i = 1; i <= TT; i++) f[x][i] = f[f[x][i - 1]][i - 1];
    for (int i = head[x]; ~i; i = nex[i])
        if(to[i] != fx) dfs(to[i], x);
}
int LCA(int x, int y) {
    if(h[x] > h[y]) swap(x, y);
    for (int i = TT; i >= 0; i--)
        if(h[f[y][i]] >= h[x]) y = f[y][i];
    if(x == y) return x;
    for (int i = TT; i >= 0; i--)
        if(f[y][i] != f[x][i])
            y = f[y][i], x = f[x][i];
    return f[x][0];
}
int ct;
void update(int l, int r, int &x, int y, int pos) {
    T[++ct] = T[y];
    T[ct].sum++;
    x = ct;
    if(l == r) return;
    int mid = (l + r) >> 1;
    if(pos <= mid) update(l, mid, T[x].l, T[y].l, pos);
    else update(mid + 1, r, T[x].r, T[y].r, pos);
}
int query(int l, int r, int x, int y, int z, int t, int k) {
    if(l == r) {
        return v[l];
    }
    int mid = (l + r) >> 1;
    int sum = T[T[x].l].sum + T[T[y].l].sum - T[T[z].l].sum - T[T[t].l].sum;
    if(sum >= k) return query(l, mid, T[x].l, T[y].l, T[z].l, T[t].l, k);
    else return query(mid + 1, r, T[x].r, T[y].r, T[z].r, T[t].r, k - sum);//*往右找就是找第k-sum小的数
}
void dfs(int u) {//*再来一遍dfs建立主席树
    update(1, tsize, root[u], root[f[u][0]], getid(val[u]));
    for (int i = head[u]; ~i; i = nex[i]) {
        int v = to[i];
        if(v != f[u][0]) dfs(v);
    }
}
int main()
{
    cin >> n >> m;
    memset(head, -1, sizeof(head));
    for (int i = 1; i <= n; i++) scanf("%d", &val[i]), v[i] = val[i];
    sort(v + 1, v + 1 + n);
    tsize = unique(v + 1, v + 1 + n) - v - 1;
    for (int i = 1; i < n; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        add(x, y); add(y, x);
    }
    TT = int(log(n) / log(2)) + 1;//树的最大深度
    int u, v, k;
    dfs(1, 0);
    dfs(1);
    int ans = 0;
    for (int i = 1; i <= m; i++) {
        scanf("%d %d %d", &u, &v, &k);
        u ^= ans;
        int lca = LCA(u, v);
        ans = query(1, tsize, root[u], root[v], root[lca], root[f[lca][0]], k);
        printf("%d\n", ans);
    }
    return 0;
}