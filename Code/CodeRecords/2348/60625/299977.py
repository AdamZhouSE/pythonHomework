#pragma GCC optimize(2)
#include <bits/stdc++.h>
using namespace std;
#define rep(i, x, y) for (int i = (x); i <= (y); ++i)
inline int read() {
    char ch = getchar();
    int x = 0, f = 1;
    while (ch < '0' || ch > '9') {
        if (ch == '-')
            f = -1;
        ch = getchar();
    }
    while ('0' <= ch && ch <= '9') {
        x = x * 10 + ch - '0';
        ch = getchar();
    }
    return x * f;
}
struct Edge {
    int from, to, cap, flow, next;
} G[200010];
int head[10010], cur[10010], tot;
int d[10010], vis[10010];
int s, t;
inline void init() {
    memset(head, -1, sizeof(head));
    tot = -1;
}
inline void add(int u, int v, int w) {
    if (w == 1) {
        G[++tot] = (Edge){ u, v, w, 0, head[u] };
        head[u] = tot;
        G[++tot] = (Edge){ v, u, 0, 0, head[v] };
        head[v] = tot;
    } else {
        G[++tot] = (Edge){ u, v, 0, 0, head[u] };
        head[u] = tot;
    }
}
inline bool BFS() {
    memset(vis, 0, sizeof(vis));
    queue<int> Q;
    Q.push(s);
    vis[s] = 1;
    d[s] = 0;
    while (!Q.empty()) {
        int x = Q.front();
        Q.pop();
        for (int i = head[x]; i != -1; i = G[i].next) {
            Edge& e = G[i];
            if (!vis[e.to] && e.cap > e.flow) {
                d[e.to] = d[x] + 1;
                vis[e.to] = 1;
                Q.push(e.to);
            }
        }
    }
    return vis[t];
}
inline int DFS(int x, int a) {
    if (x == t || a == 0)
        return a;
    int flow = 0, f;
    for (int& i = cur[x]; i != -1; i = G[i].next) {
        Edge& e = G[i];
        if (d[e.to] == d[x] + 1 && (f = DFS(e.to, min(a, e.cap - e.flow))) > 0) {
            e.flow += f;
            G[i ^ 1].flow -= f;
            flow += f;
            a -= f;
            if (a == 0)
                break;
        }
    }
    return flow;
}
inline int ans() {
    int flow = 0;
    while (BFS()) {
        for (int i = s; i <= t; i++) cur[i] = head[i];
        flow += DFS(s, 1e9);
    }
    return flow;
}
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
int num[110][110], tt;
char S[110][110];
int mat[10010];
bool vis1[10010];
inline void dfs(int x) {
    vis1[x] = 1;
    for (int i = head[x]; i != -1; i = G[i].next) {
        if (!vis1[mat[G[i].to]]) {
            dfs(mat[G[i].to]);
        }
    }
}
int main() {
    //	freopen("B.in", "r", stdin);
    int n = read(), m = read();
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            num[i][j] = ++tt;
        }
    }
    init();
    s = 0, t = tt + 1;
    //	cerr << 233 << endl;
    for (int i = 1; i <= n; ++i) {
        scanf("%s", S[i] + 1);
    }
    //	cerr << 233 << endl;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            if (S[i][j] == '.') {
                if (i + j & 1)
                    add(s, num[i][j], 1);
                else
                    add(num[i][j], t, 1);
                if (i + j & 1) {
                    rep(k, 0, 3) {
                        int x = i + dx[k], y = j + dy[k];
                        if (x < 1 || y < 1 || x > n || y > m)
                            continue;
                        if (S[x][y] == '#')
                            continue;
                        add(num[i][j], num[x][y], 1);
                        // if(num[i][j] <= 3)cerr << tot << " " << num[x][y] << endl;
                    }
                }
            }
    }
    ans();
    for (int i = 0; i <= tot; ++i) {
        //		if(i == 0) cerr << G[i].from << " " << G[i].to << endl;
        if (G[i].from == s) {
            if (G[i].flow == 1) {
                for (int j = head[G[i].to]; j != -1; j = G[j].next) {
                    if (G[j].flow == 1) {
                        mat[G[i].to] = G[j].to;
                        mat[G[j].to] = G[i].to;
                        //						printf("%d %d\n", G[i].to, G[j].to);
                    }
                }
            }
        }
    }
    tot = -1;
    memset(head, -1, sizeof(head));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j)
            if (S[i][j] == '.') {
                if (i + j & 1) {
                    rep(k, 0, 3) {
                        int x = i + dx[k], y = j + dy[k];
                        if (x < 1 || y < 1 || x > n || y > m)
                            continue;
                        if (S[x][y] == '#')
                            continue;
                        add(num[i][j], num[x][y], 0);
                        add(num[x][y], num[i][j], 0);
                    }
                }
            }
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (S[i][j] == '#')
                continue;
            if (!mat[num[i][j]])
                dfs(num[i][j]);
        }
    }
    int res = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (vis1[num[i][j]])
                ++res;
        }
    }
    printf("%d\n", res);
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (vis1[num[i][j]]) {
                printf("%d %d\n", i, j);
            }
        }
    }
}