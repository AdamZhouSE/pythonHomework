#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int n, m, r, np, nq, ans, tot;
int p[210], q[210], v[210][210], fa[210], vis[210];
inline int rd() {
    int ret = 0;
    char gc = getchar();
    while (gc < '0' || gc > '9') gc = getchar();
    while (gc >= '0' && gc <= '9') ret = ret * 10 + gc - '0', gc = getchar();
    return ret;
}
void dfs(int x) {
    vis[x] = 1;
    for (int i = 1; i <= np; i++)
        if (fa[p[i]] == x)
            dfs(p[i]);
}
int main() {
    memset(v, 0x3f, sizeof(v));
    np = tot = n = rd(), m = rd(), r = rd();
    int i, j, a, b, c, x, y;
    for (i = 1; i <= n; i++) p[i] = i;
    for (i = 1; i <= m; i++) {
        a = rd(), b = rd(), c = rd();
        if (a != b)
            v[a][b] = min(v[a][b], c);
    }
    v[0][r] = 0;
    while (1) {
        memset(fa, 0, sizeof(fa));
        for (i = 1; i <= np; i++) {
            x = p[i];
            for (j = 1; j <= np; j++)
                if (v[p[j]][x] < v[fa[x]][x])
                    fa[x] = p[j];
            if (v[fa[x]][x] > 1e8) {
                printf("-1");
                return 0;
            }
        }
        memset(vis, 0, sizeof(vis));
        dfs(r);
        for (i = 1; i <= np; i++)
            if (!vis[p[i]]) {
                for (j = p[i]; !vis[j]; j = fa[j]) vis[j] = 1;
                for (; vis[j] == 1; j = fa[j]) vis[j] = 2, ans += v[fa[j]][j];
                break;
            }
        if (i == np + 1)
            break;
        tot++;
        for (i = 1; i <= np; i++)
            if (vis[p[i]] != 2)
                for (x = p[i], j = 1; j <= np; j++)
                    if (vis[p[j]] == 2)
                        y = p[j], v[x][tot] = min(v[x][tot], v[x][y] - v[fa[y]][y]),
                        v[tot][x] = min(v[tot][x], v[y][x]);
        for (nq = 0, i = 1; i <= np; i++)
            if (vis[p[i]] != 2)
                q[++nq] = p[i];
        q[++nq] = tot;
        memcpy(p, q, sizeof(q[0]) * (nq + 1));
        np = nq;
    }
    for (i = 1; i <= np; i++) ans += v[fa[p[i]]][p[i]];
    printf("%d", ans);
    return 0;
}