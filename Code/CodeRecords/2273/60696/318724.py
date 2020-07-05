#include <bits/stdc++.h>
#define pb push_back
using namespace std;
char gc() {
    static char buf[1 << 15], *p1, *p2;
    if (p1 == p2)
        p2 = (p1 = buf) + fread(buf, 1, 1 << 15, stdin);
    if (p1 == p2)
        return EOF;
    else
        return *(p1++);
}
int rd() {
    int rx = 0, fx = 1;
    char c = gc();
    while (c < 48 || c > 57) {
        if (c == '-')
            fx = -1;
        c = gc();
    }
    while (c >= 48 && c <= 57) {
        rx = rx * 10 + c - 48;
        c = gc();
    }
    return rx * fx;
}
const int N = 4e4 + 50, H = 1e6 + 50, U = 1e8 + 7e6 + 10;
int n, K, opt, cur, ans;
int *f[N], *g[N], *lc, buf[U];
int fa[N], a[N], b[N], dfn[N][2], dy[N], siz[N], tag[N], wdt[N];
vector<int> e[N];
void dfs(int x, int nf) {
    int vsi, i, v;
    siz[x] = 1;
    wdt[x] = wdt[nf] + b[x];
    vsi = e[x].size();
    if (opt == 0) {
        for (i = 0; i < vsi; i++) {
            v = e[x][i];
            if (v == nf)
                continue;
            dfs(v, x);
            siz[x] += siz[v];
        }
    } else {
        for (i = vsi - 1; i >= 0; i--) {
            v = e[x][i];
            if (v == nf)
                continue;
            dfs(v, x);
            siz[x] += siz[v];
        }
    }
    dfn[x][opt] = ++cur;
    dy[cur] = x;
}
struct Node {
    int id, w;
};
Node p[H];
void solve(int *dp[N]) {
    // puts("solve");
    int i, j, x, si, l, r;
    struct Node now;
    cur = 0;
    dfs(1, 0);
    for (i = 1; i <= n * 2; i++) {
        x = dy[i];
        si = siz[x];
        l = r = 0;
        // printf("U%d\n",a[x]);
        for (j = 0; j <= K; j++) {
            dp[i][j] = dp[i - si][j];
            while (l < r && j - p[l + 1].id > a[x]) l++;
            if (r > l) {
                dp[i][j] = max(dp[i][j], p[l + 1].w + b[x] * j);
            }
            now.id = j;
            now.w = dp[i - 1][j] - b[x] * j;
            while (r > l && p[r].w <= now.w) r--;
            p[++r] = now;
            // printf("X%d  #%d %d  %d\n",x,i,j,dp[i][j]);
        }
    }
}
void Solve() {
    int i, j, x, y;
    n = rd();
    K = rd();
    memset(buf, 0, sizeof(buf));
    lc = buf;
    for (i = 0; i <= n * 2 + 2; i++) {
        f[i] = lc;
        lc += K + 5;
    }
    lc += n * 2 + K * 2 + 10;
    for (i = 0; i <= n * 2 + 2; i++) {
        g[i] = lc;
        lc += K + 5;
    }
    memset(tag, 0, sizeof(tag));
    for (i = 1; i <= n * 2; i++) e[i].clear();
    for (i = 1; i <= n; i++) fa[i] = rd(), a[i] = rd(), b[i] = rd();
    for (i = 1; i <= n; i++) {
        if (fa[i] != 0)
            tag[fa[i]] = 1;
        a[i + n] = a[i] - 1;
        a[i] = 1;
        b[i + n] = b[i];
        e[i].pb(i + n);
        if (i != 1)
            e[fa[i]].pb(i);
    }
    opt = 0;
    solve(f);
    opt = 1;
    solve(g);
    ans = 0;
    for (i = 1; i <= n; i++) {
        if (tag[i] == 0) {
            // printf("try %d  %d %d\n",i,dfn[i][0],dfn[i][1]);
            x = dfn[i][0] - 1;
            y = dfn[i + n][1] - 1;
            // printf("wdt %d\n",wdt[i]);
            for (j = 0; j <= K; j++) ans = max(ans, f[x][j] + g[y][K - j] + wdt[i]);
        }
    }
    printf("%d\n", ans);
}
int main() {
    int T;
    T = rd();
    while (T--) Solve();
    return 0;
}