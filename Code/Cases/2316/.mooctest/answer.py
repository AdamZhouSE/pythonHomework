#include <bits/stdc++.h>
using namespace std;
const double eps = 1e-8;
const int N = 305, M = N * N * 3, Inf = 1 << 30;
int n, a[N][N], b[N][N];
namespace flow {
int head[N], nxt[M], to[M], wei[M], s, t, tot;
bool vis[N];
double cost[M], dis[N], ans;
void addedge(int u, int v, int w, double c) {
    nxt[++tot] = head[u], head[u] = tot, to[tot] = v, wei[tot] = w, cost[tot] = c;
    nxt[++tot] = head[v], head[v] = tot, to[tot] = u, wei[tot] = 0, cost[tot] = -c;
}
bool spfa() {
    memset(vis, false, sizeof(vis));
    for (int i = 1; i <= t; ++i) dis[i] = 1e20;
    queue<int> q;
    dis[t] = 0, q.push(t);
    while (!q.empty()) {
        int u = q.front();
        vis[u] = false, q.pop();
        for (int e = head[u]; e; e = nxt[e])
            if (wei[e ^ 1] && dis[to[e]] > dis[u] - cost[e]) {
                dis[to[e]] = dis[u] - cost[e];
                if (!vis[to[e]])
                    vis[to[e]] = true, q.push(to[e]);
            }
    }
    return dis[s] != 1e20;
}
int dfs(int u, int mx) {
    vis[u] = true;
    if (u == t)
        return mx;
    int l = mx;
    for (int e = head[u]; e && l; e = nxt[e])
        if (!vis[to[e]] && wei[e] > 0 && abs(dis[to[e]] - (dis[u] - cost[e]) < eps)) {
            int f = dfs(to[e], min(l, wei[e]));
            ans += cost[e] * f;
            l -= f, wei[e] -= f, wei[e ^ 1] += f;
        }
    return mx - l;
}
double solve() {
    ans = 0.0;
    while (spfa()) do {
            memset(vis, false, sizeof(vis));
            dfs(s, Inf);
        } while (vis[t]);
    return ans;
}
}  // namespace flow
using flow::addedge;
using flow::solve;
bool check(double x) {
    memset(flow::head, 0, sizeof(flow::head)), flow::tot = 1;
    for (int i = 1; i <= n; ++i) addedge(flow::s, i, 1, 0), addedge(i + n, flow::t, 1, 0);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) addedge(i, j + n, 1, x * b[i][j] - a[i][j]);
    bool b = solve() < eps;
    return b;
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) scanf("%d", &a[i][j]);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) scanf("%d", &b[i][j]);
    flow::s = 2 * n + 1, flow::t = flow::s + 1;
    double l = 0, r = 1e6, ans = -1.0;
    while (r - l > eps) {
        double mid = (l + r) / 2.0;
        check(mid) ? ans = l = mid : r = mid;
    }
    printf("%.6lf", ans);
}