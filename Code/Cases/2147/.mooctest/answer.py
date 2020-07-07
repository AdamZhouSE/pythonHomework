#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;
int gi() {
    int x = 0, w = 1;
    char ch = getchar();
    while ((ch < '0' || ch > '9') && ch != '-') ch = getchar();
    if (ch == '-')
        w = 0, ch = getchar();
    while (ch >= '0' && ch <= '9') x = (x << 3) + (x << 1) + ch - '0', ch = getchar();
    return w ? x : -x;
}
const int N = 2e5 + 5;
struct Graph {
    int to[N], nxt[N], hd[N], cnt;
    void link(int u, int v) {
        to[++cnt] = v;
        nxt[cnt] = hd[u];
        hd[u] = cnt;
        to[++cnt] = u;
        nxt[cnt] = hd[v];
        hd[v] = cnt;
    }
} G, F;
int n, m, S, A, B, dep[N], vis[N], ans[N];
queue<int> Q;
int main() {
    n = gi();
    m = gi();
    S = gi();
    A = gi();
    B = gi();
    for (int i = 1; i <= m; ++i) {
        int u = gi(), v = gi();
        G.link(u, v);
        F.link(u, v);
    }
    dep[S] = 1;
    Q.push(S);
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        for (int e = G.hd[u]; e; e = G.nxt[e]) {
            int v = G.to[e];
            if (!dep[v])
                dep[v] = dep[u] + 1, Q.push(v);
        }
    }
    for (int i = 1; i <= n; ++i) --dep[i], ans[i] = min(dep[i] * A, (dep[i] >> 1) * B + (dep[i] & 1) * A);
    memset(dep, 0, sizeof(dep));
    dep[S] = 1;
    Q.push(S);
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        for (int e = G.hd[u]; e; e = G.nxt[e]) vis[G.to[e]] = u;
        for (int e = G.hd[u]; e; e = G.nxt[e]) {
            int v = G.to[e];
            for (int i = F.hd[v], las = 0; i; i = F.nxt[i]) {
                int w = F.to[i];
                if (vis[w] == u) {
                    las = i;
                    continue;
                }
                if (!dep[w])
                    dep[w] = dep[u] + 1, Q.push(w);
                if (!las)
                    F.hd[v] = F.nxt[F.hd[v]];
                else
                    F.nxt[las] = F.nxt[i];
            }
        }
    }
    for (int i = 1; i <= n; ++i)
        if (dep[i])
            --dep[i], ans[i] = min(ans[i], dep[i] * B);
    for (int i = 1; i <= n; ++i) printf("%d\n", ans[i]);
    return 0;
}