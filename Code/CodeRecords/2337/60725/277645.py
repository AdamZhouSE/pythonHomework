#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
inline int read() {
    int res = 0; bool bo = 0; char c;
    while (((c = getchar()) < '0' || c > '9') && c != '-');
    if (c == '-') bo = 1; else res = c - 48;
    while ((c = getchar()) >= '0' && c <= '9')
        res = (res << 3) + (res << 1) + (c - 48);
    return bo ? ~res + 1 : res;
}
inline char get() {
    char c; while ((c = getchar()) != '*' && c != 'x' && c != '#');
    return c;
}
const int N = 55, M = 2505;
int n, m, tot, ecnt, nxt[M], adj[M], go[M], my[M], row[N][N], col[N][N];
bool vis[M]; char a[N][N];
void add_edge(int u, int v) {
    nxt[++ecnt] = adj[u]; adj[u] = ecnt; go[ecnt] = v;
}
bool dfs(int u) {
    for (int e = adj[u], v; e; e = nxt[e])
        if (!vis[v = go[e]]) {
            vis[v] = 1;
            if (!my[v] || dfs(my[v])) {
                my[v] = u;
                return 1;
            }
        }
    return 0;
}
int solve() {
    int i, ans = 0;
    for (i = 1; i <= tot; i++) {
        memset(vis, 0, sizeof(vis));
        if (dfs(i)) ans++;
    }
    return ans;
}
int main() {
    int i, j; n = read(); m = read();
    for (i = 1; i <= n; i++) for (j = 1; j <= m; j++)
        a[i][j] = get();
    for (i = 1; i <= n; i++) for (j = 1; j <= m; j++) {
        if (a[i][j] == '#') continue;
        if (j == 1 || a[i][j - 1] == '#') tot++;
        row[i][j] = tot;
    }
    for (j = 1; j <= m; j++) for (i = 1; i <= n; i++) {
        if (a[i][j] == '#') continue;
        if (i == 1 || a[i - 1][j] == '#') tot++;
        col[i][j] = tot;
    }
    for (i = 1; i <= n; i++) for (j = 1; j <= m; j++) {
        if (a[i][j] != '*') continue;
        add_edge(row[i][j], col[i][j]);
    }
    printf("%d\n%s", solve());
    
    return 0;
}