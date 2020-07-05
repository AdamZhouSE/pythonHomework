#include <bits/stdc++.h>
#define fp(i, a, b) for (register int i = a, I = b + 1; i < I; ++i)
#define fd(i, a, b) for (register int i = a, I = b - 1; i > I; --i)
#define go(u) for (register int i = fi[u], v = e[i].to; i; v = e[i = e[i].nx].to)
#define file(s) freopen(s ".in", "r", stdin), freopen(s ".out", "w", stdout)
template <class T>
inline bool cmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }
template <class T>
inline bool cmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
using namespace std;
const int N = 105, M = 1005, P = 31011;
typedef int arr[N];
struct eg
{
    int u, v, w;
} e[M];
int n, m, ans = 1;
arr fa, bl, vis, g[N], G[N];
vector<int> s[N];
int gf(int u, int *fa) { return fa[u] == u ? u : fa[u] = gf(fa[u], fa); }//find并查集
inline int pls(int a, int b) { return a += b, a >= P ? a - P : a; }//模数不为质数的操作
inline int sub(int a, int b) { return a -= b, a < 0 ? a + P : a; }
inline int det(int n)//返回缩点的生成树个数
{
    int a, b, t, f = 1, tp = 1;
    fp(i, 1, n) fp(j, 1, n) G[i][j] = pls(P, G[i][j]);
    fp(i, 1, n)
    {
        fp(j, i + 1, n)
        {
            a = G[i][i], b = G[j][i];
            while (b)
            {
                t = a / b;
                a %= b;
                swap(a, b);
                fp(k, i, n) G[i][k] = sub(G[i][k], t * G[j][k] % P);
                fp(k, i, n) swap(G[i][k], G[j][k]);
                f = -f;
            }
        }
        if (!G[i][i])
            return 0;
        tp = tp * G[i][i] % P;
    }
    return pls(P, f * tp);
}
inline void calc()//合并联通块形成缩点
{
    fp(i, 1, n) if (vis[i])
    {
        s[gf(i, fa)].push_back(i);
        vis[i] = 0;
    }
    fp(i, 1, n) if (s[i].size() > 1)
    {
        int t = s[i].size(), *a = s[i].data();
        memset(G, 0, sizeof G);
        fp(j, 1, t) fp(k, j + 1, t)
        {
            int u = a[j - 1], v = a[k - 1];
            if (g[u][v])
            {
                G[j][k] = G[k][j] = -g[u][v];
                G[j][j] += g[u][v], G[k][k] += g[u][v];
            }
        }
        ans = ans * det(t - 1) % P;
        fp(j, 1, t) bl[a[j - 1]] = i;//属于同一联通块
    }
    fp(i, 1, n) s[i].clear(), fa[i] = bl[i] = gf(i, bl);
}
inline bool cmp(const eg &a, const eg &b) { return a.w < b.w; }
int main()
{
#ifndef ONLINE_JUDGE
    file("s");
#endif
    scanf("%d%d", &n, &m);
    fp(i, 1, n) fa[i] = bl[i] = i;
    fp(i, 1, m) scanf("%d%d%d", &e[i].u, &e[i].v, &e[i].w);
    sort(e + 1, e + m + 1, cmp);
    e[0] = e[1];
    fp(i, 1, m)
    {
        //发现不相同的边界点就计算处理
        if (e[i].w ^ e[i - 1].w)
            calc();
            //同一权值合并
        int u = gf(e[i].u, bl), v = gf(e[i].v, bl);
        if (u ^ v)
        {
            vis[u] = vis[v] = 1;
            ++g[u][v], ++g[v][u];
            fa[gf(u, fa)] = gf(v, fa);
        }
    }
    calc();
    fp(i, 2, n) if (bl[i] ^ bl[i - 1]) return puts("0"), 0;
    printf("%d", ans);
    return 0;
}
