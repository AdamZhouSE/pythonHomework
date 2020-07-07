#include <bits/stdc++.h>

using namespace std;

inline int read() {
    int x = 0, f = 1;
    char p = getchar();
    while (!isdigit(p)) {
        if (p == '-')
            f = -1;
        p = getchar();
    }
    while (isdigit(p)) x = (x << 3) + (x << 1) + (p ^ 48), p = getchar();
    return x * f;
}

const int maxn = 105, maxm = 1e4 + 5;

int n, m, a[maxn][maxn], id[maxn][maxn], tot, cnt, head[maxm], matched[maxm];
int ver[maxm << 2], nxt[maxm << 2], vis[maxm], ans, flag[maxn][maxn];

inline void add(int x, int y) {
    nxt[++cnt] = head[x];
    head[x] = cnt;
    ver[cnt] = y;
}

inline bool dfs(int x) {
    for (int i = head[x]; i; i = nxt[i]) {
        int y = ver[i];
        if (vis[y])
            continue;
        vis[y] = 1;
        if (!matched[y] || dfs(matched[y])) {
            matched[y] = x;
            return 1;
        }
    }
    return 0;
}

int main() {
    n = read();
    m = read();
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            char opt;
            cin >> opt;
            if (opt == '.')
                a[i][j] = 0, id[i][j] = ++tot;
            else
                a[i][j] = 1;
        }
    for (int i = 1; i <= n; i++)
        for (int j = 1; j < m; j++)
            if (a[i][j] == 0 && a[i][j + 1] == 0)
                add(id[i][j], id[i][j + 1]), add(id[i][j + 1], id[i][j]);
    for (int i = 1; i <= m; i++)
        for (int j = 1; j < n; j++)
            if (a[j][i] == 0 && a[j + 1][i] == 0)
                add(id[j][i], id[j + 1][i]), add(id[j + 1][i], id[j][i]);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == 0 && ((i + j) % 2 == 0)) {
                memset(vis, 0, sizeof(vis));
                dfs(id[i][j]);
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == 0 && ((i + j) % 2 == 1)) {
                if (!matched[id[i][j]])
                    flag[i][j] = 1;
                else {
                    memset(vis, 0, sizeof(vis));
                    vis[id[i][j]] = 1;
                    if (dfs(matched[id[i][j]])) {
                        matched[id[i][j]] = 0;
                        flag[i][j] = 1;
                    }
                }
            }
        }
    }
    memset(matched, 0, sizeof(matched));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == 0 && ((i + j) % 2 == 1)) {
                memset(vis, 0, sizeof(vis));
                if (dfs(id[i][j]))
                    ans++;
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == 0 && ((i + j) % 2 == 0)) {
                if (!matched[id[i][j]])
                    flag[i][j] = 1;
                else {
                    memset(vis, 0, sizeof(vis));
                    vis[id[i][j]] = 1;
                    if (dfs(matched[id[i][j]])) {
                        matched[id[i][j]] = 0;
                        flag[i][j] = 1;
                    }
                }
            }
        }
    }
    ans = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (flag[i][j])
                ans++;
    cout << ans << endl;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            if (flag[i][j])
                printf("%d %d\n", i, j);
    return 0;
}