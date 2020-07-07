#include <bits/stdc++.h>
using namespace std;

const int maxn = 30010;
int n, m, K, cur, rt, pre[maxn], dist[maxn], len[maxn], vis[maxn];
int ans1, ans2, mx[maxn], dep[maxn], sz[maxn], num[maxn];
struct edge {
    int v, w;
};
vector<edge> G[maxn], H[maxn];
queue<int> q;

void spfa() {
    memset(dist, 0x3f, sizeof(dist));
    q.push(1), dist[1] = 0;
    while (!q.empty()) {
        int v = q.front();
        q.pop(), vis[v] = 0;
        for (int i = 0, u; i < H[v].size(); i++) {
            if (dist[u = H[v][i].v] > dist[v] + H[v][i].w) {
                dist[u] = dist[pre[u] = v] + H[v][i].w;
                if (!vis[u])
                    q.push(u), vis[u] = 1;
            } else if (dist[u] == dist[v] + H[v][i].w) {
                if (v < pre[u])
                    pre[u] = v;
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < H[i].size(); j++) {
            if (i == pre[H[i][j].v] || pre[i] == H[i][j].v) {
                if (vis[H[i][j].v])
                    continue;
                H[i][j].w = abs(dist[i] - dist[H[i][j].v]);
                vis[H[i][j].v] = 1, G[i].push_back(H[i][j]);
            }
        }
        for (int j = 0; j < H[i].size(); j++) {
            if (i == pre[H[i][j].v] || pre[i] == H[i][j].v)
                vis[H[i][j].v] = 0;
        }
    }
}

void get_root(int v, int f) {
    sz[v] = 1, mx[v] = 0;
    for (int i = 0, u; i < G[v].size(); i++) {
        if ((u = G[v][i].v) == f || vis[u])
            continue;
        get_root(u, v), sz[v] += sz[u], mx[v] = max(mx[v], sz[u]);
    }
    mx[v] = max(mx[v], cur - mx[v]);
    if (mx[v] < mx[rt])
        rt = v;
}

void calc(int v, int f) {
    if (dep[v] <= K) {
        int tmp = dist[v] + len[K - dep[v]];
        if (tmp > ans1)
            ans1 = tmp, ans2 = 0;
        if (tmp == ans1)
            ans2 += num[K - dep[v]];
    }
    for (int i = 0, u; i < G[v].size(); i++) {
        if ((u = G[v][i].v) == f || vis[u])
            continue;
        dist[u] = dist[v] + G[v][i].w;
        dep[u] = dep[v] + 1, calc(u, v);
    }
}

void upd(int v, int f, int t) {
    if (dep[v] <= K) {
        if (t) {
            if (dist[v] > len[dep[v]])
                len[dep[v]] = dist[v], num[dep[v]] = 0;
            if (dist[v] == len[dep[v]])
                num[dep[v]]++;
        } else {
            len[dep[v]] = num[dep[v]] = 0;
        }
    }
    for (int i = 0, u; i < G[v].size(); i++) {
        if ((u = G[v][i].v) ^ f && !vis[u])
            upd(u, v, t);
    }
}

void divide(int v) {
    vis[v] = num[0] = 1, len[0] = 0;
    for (int i = 0, u; i < G[v].size(); i++) {
        if (vis[u = G[v][i].v])
            continue;
        dist[u] = G[v][i].w, dep[u] = 1;
        calc(u, v), upd(u, v, 1);
    }
    for (int i = 0, u; i < G[v].size(); i++) {
        if (!vis[u = G[v][i].v])
            upd(u, v, 0);
    }
    for (int i = 0, u; i < G[v].size(); i++) {
        if (vis[u = G[v][i].v])
            continue;
        cur = sz[u], get_root(u, rt = 0), divide(rt);
    }
}

int main() {
    scanf("%d %d %d", &n, &m, &K), K--;
    for (int i = 1, u, v, w; i <= m; i++) {
        scanf("%d %d %d", &u, &v, &w);
        H[u].push_back((edge){ v, w }), H[v].push_back((edge){ u, w });
    }
    spfa(), cur = mx[rt] = n, get_root(1, 0), divide(rt);
    printf("%d %d\n", ans1, ans2);
    return 0;
}