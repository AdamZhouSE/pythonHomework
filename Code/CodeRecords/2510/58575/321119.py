#include <bits/stdc++.h>
using namespace std;
#define mem(a, b) memset(a, b, sizeof(a))
#define lson l, m, rt << 1
#define rson m + 1, r, rt << 1 | 1
const int N = 2e5 + 10;
int sum[N << 2], lazy[N << 2]; //线段树求和
int n, m, r, mod;              //节点数，操作数，根节点，模数
int first[N], tot;             //邻接表
//分别为:重儿子，每个节点新编号，父亲，编号，深度，子树个数，所在重链的顶部
int son[N], id[N], fa[N], cnt, dep[N], siz[N], top[N];
int w[N], wt[N]; //初始点权,新编号点权
int res = 0;     //查询答案
struct edge
{
    int v, next;
} e[N];
void add_edge(int u, int v)
{
    e[tot].v = v;
    e[tot].next = first[u];
    first[u] = tot++;
}
void init()
{
    mem(first, -1);
    tot = 0;
    cnt = 0;
}
int pushup(int rt)
{
    sum[rt] = (sum[rt << 1] + sum[rt << 1 | 1]) % mod;
}
void pushdown(int rt, int m) //下放lazy标记
{
    if (lazy[rt])
    {
        lazy[rt << 1] += lazy[rt];                 //给左儿子下放lazy
        lazy[rt << 1 | 1] += lazy[rt];             //给右儿子下放lazy
        sum[rt << 1] += lazy[rt] * (m - (m >> 1)); //更新sum
        sum[rt << 1] %= mod;
        sum[rt << 1 | 1] += lazy[rt] * (m >> 1);
        sum[rt << 1 | 1] %= mod;
        lazy[rt] = 0;
    }
}
void build(int l, int r, int rt)
{
    lazy[rt] = 0;
    if (l == r)
    {
        sum[rt] = wt[l]; //新的编号点权
        sum[rt] %= mod;
        return;
    }
    int m = (l + r) >> 1;
    build(lson);
    build(rson);
    pushup(rt);
}
void update(int L, int R, int c, int l, int r, int rt)
{
    if (L <= l && r <= R)
    {
        lazy[rt] += c;
        sum[rt] += c * (r - l + 1);
        sum[rt] %= mod;
        return;
    }
    pushdown(rt, r - l + 1);
    int m = (l + r) >> 1;
    if (L <= m)
        update(L, R, c, lson);
    if (R > m)
        update(L, R, c, rson);
    pushup(rt);
}
void query(int L, int R, int l, int r, int rt)
{
    if (L <= l && r <= R)
    {
        res += sum[rt];
        res %= mod;
        return;
    }
    pushdown(rt, r - l + 1);
    int m = (l + r) >> 1;
    if (L <= m)
        query(L, R, lson);
    if (R > m)
        query(L, R, rson);
}
//----------------------------------------------------------------
//处理出fa[],dep[],siz[],son[]
void dfs1(int u, int f, int deep)
{
    dep[u] = deep;   //标记深度
    fa[u] = f;       //标记节点的父亲
    siz[u] = 1;      //记录每个节点子树大小
    int maxson = -1; //记录重儿子数量
    for (int i = first[u]; ~i; i = e[i].next)
    {
        int v = e[i].v;
        if (v == f)
            continue;
        dfs1(v, u, deep + 1);
        siz[u] += siz[v];
        if (siz[v] > maxson) //儿子里最多siz就是重儿子
        {
            son[u] = v; //标记u的重儿子为v
            maxson = siz[v];
        }
    }
}

//处理出top[],wt[],id[]
void dfs2(int u, int topf)
{
    id[u] = ++cnt;  //每个节点的新编号
    wt[cnt] = w[u]; //新编号的对应权值
    top[u] = topf;  //标记每个重链的顶端
    if (!son[u])    //没有儿子时返回
        return;
    dfs2(son[u], topf); //搜索下一个重儿子
    for (int i = first[u]; ~i; i = e[i].next)
    {
        int v = e[i].v;
        if (v == fa[u] || v == son[u]) //处理轻儿子
            continue;
        dfs2(v, v); //每一个轻儿子都有一个从自己开始的链
    }
}
void updrange(int x, int y, int k)
{
    k %= mod;
    while (top[x] != top[y])
    {
        if (dep[top[x]] < dep[top[y]]) //使x深度较大
            swap(x, y);
        update(id[top[x]], id[x], k, 1, n, 1);
        x = fa[top[x]];
    }
    if (dep[x] > dep[y]) //使x深度较小
        swap(x, y);
    update(id[x], id[y], k, 1, n, 1);
}
int qrange(int x, int y)
{
    int ans = 0;
    while (top[x] != top[y]) //当两个点不在同一条链上
    {
        if (dep[top[x]] < dep[top[y]]) //使x深度较大
            swap(x, y);
        res = 0;
        query(id[top[x]], id[x], 1, n, 1);
        //ans加上x点到x所在链顶端这一段区间的点权和
        ans += res;
        ans %= mod;
        x = fa[top[x]]; //x跳到x所在链顶端的这个点的上面一个点
    }
    //当两个点处于同一条链
    if (dep[x] > dep[y]) //使x深度较小
        swap(x, y);
    res = 0;
    query(id[x], id[y], 1, n, 1);
    ans += res;
    return ans % mod;
}
void upson(int x, int k)
{
    update(id[x], id[x] + siz[x] - 1, k, 1, n, 1); //子树区间右端点为id[x]+siz[x]-1
}
int qson(int x)
{
    res = 0;
    query(id[x], id[x] + siz[x] - 1, 1, n, 1);
    return res;
}
int main()
{
    // freopen("in.txt", "r", stdin);
    int u, v;
    scanf("%d%d%d%d", &n, &m, &r, &mod);
    init();
    for (int i = 1; i <= n; i++)
        scanf("%d", &w[i]);
    for (int i = 1; i <= n - 1; i++)
    {
        scanf("%d%d", &u, &v);
        add_edge(u, v);
        add_edge(v, u);
    }
    dfs1(r, 0, 1);
    dfs2(r, r);
    build(1, n, 1); //用新点权建立线段树
    while (m--)
    {
        int op, x, y, z;
        scanf("%d", &op);
        if (op == 1)
        {
            scanf("%d%d%d", &x, &y, &z);
            updrange(x, y, z);
        }
        else if (op == 2)
        {
            scanf("%d%d", &x, &y);
            printf("%d\n", qrange(x, y));
        }
        else if (op == 3)
        {
            scanf("%d%d", &x, &z);
            upson(x, z);
        }
        else if (op == 4)
        {
            scanf("%d", &x);
            printf("%d\n", qson(x));
        }
    }
    return 0;
}