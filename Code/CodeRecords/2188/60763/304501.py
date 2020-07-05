#include <bits/stdc++.h>
using namespace std;

const int maxn = 1000005, mod = 1e9 + 7;

int pow2[maxn];
int n, m;

struct edge
{
    int to, next;
} e[maxn];
int h[maxn], tot;

char S[maxn];
int dfn[maxn], low[maxn], sz[maxn], bel[maxn], flag[maxn], sub[maxn], cut[maxn], deg[maxn], now, Time;

inline int gi()
{
    char c = getchar();
    while (c < '0' || c > '9') c = getchar();
    int sum = 0;
    while ('0' <= c && c <= '9') sum = sum * 10 + c - 48, c = getchar();
    return sum;
}

inline void add(int u, int v)
{
    e[++tot] = (edge) {v, h[u]}; h[u] = tot; ++deg[u];
    e[++tot] = (edge) {u, h[v]}; h[v] = tot; ++deg[v];
}

void tarjan(int u, int fa = 0)
{
    low[u] = dfn[u] = ++Time;
    flag[u] = 1; sz[u] = S[u] == '1';
    bel[u] = now;
    for (int i = h[u], v; v = e[i].to, i; i = e[i].next)
        if (!dfn[v]) {
            tarjan(v, u);
            sz[u] += sz[v];
            if (low[v] >= dfn[u]) {
                ++cut[u]; flag[u] &= (sz[v] & 1) == 0;
                sub[u] += sz[v];
            } else low[u] = min(low[u], low[v]);
        } else if (v != fa) low[u] = min(low[u], dfn[v]);
    if (!fa) --cut[u];
}

int main()
{
    pow2[0] = 1;
    for (int i = 1; i <= 100000; ++i) pow2[i] = pow2[i - 1] * 2 % mod;

    int T = gi();
    while (T--) {
        n = gi(); m = gi();
        memset(sz + 1, 0, sizeof(int) * n);
        memset(deg + 1, 0, sizeof(int) * n);
        memset(sub + 1, 0, sizeof(int) * n);
        memset(cut + 1, 0, sizeof(int) * n);
        memset(h + 1, 0, sizeof(int) * n); tot = 0;
        memset(dfn + 1, 0, sizeof(int) * n); Time = 0;
        for (int i = 1; i <= m; ++i) add(gi(), gi());
        scanf("%s", S + 1);

        int cnt = 0, cnt_odd = 0;
        for (int i = 1; i <= n; ++i)
            if (!dfn[i]) {
                now = i;
                tarjan(i); ++cnt;
                cnt_odd += sz[i] & 1;
            }

        int ans = m - n + cnt;
        printf("%d", cnt_odd ? 0 : pow2[ans]);
        for (int i = 1; i <= n; ++i) {
            if (!deg[i]) printf(" %d", cnt_odd - sz[i] == 0 ? pow2[ans] : 0);
            else {
                if (flag[i] && (((sz[bel[i]] - (S[i] == '1') - sub[i]) & 1) == 0) && cnt_odd - (sz[bel[i]] & 1) == 0)
                    printf(" %d", pow2[ans - deg[i] + 1 + cut[i]]);
                else printf(" 0");
            }
        }
        puts("");
    }

    return 0;
}