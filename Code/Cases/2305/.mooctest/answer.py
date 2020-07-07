#include <cstdio>
#include <queue>

inline int min(int a, int b) { return a < b ? a : b; }

const int inf = 1e9;

const int N = 4e4 + 5;

const int M = 1e4 + 5;

int m, c, n1, n2, _s, _t, pos_f[M], pos_c[M];

int pos_a[N], pos_b[N], node_cnt;

int h[2 * N + 2 * M], edge_cnt = 1, cur[2 * N + 2 * M], d[2 * N + 2 * M];

struct Edge {
    int to, nex, f;
} e[N * 12];

inline void add_edge(int u, int v, int w) {
    e[++edge_cnt] = (Edge){ v, h[u], w };
    h[u] = edge_cnt;
    e[++edge_cnt] = (Edge){ u, h[v], 0 };
    h[v] = edge_cnt;
}

bool bfs() {
    for (int u = 1; u <= node_cnt; ++u) d[u] = inf, cur[u] = h[u];
    std::queue<int> Q;
    d[_s] = 0;
    Q.push(_s);
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();
        for (int i = h[u]; i; i = e[i].nex)
            if (e[i].f) {
                int v = e[i].to;
                if (d[v] <= d[u] + 1)
                    continue;
                d[v] = d[u] + 1;
                Q.push(v);
            }
    }
    return d[_t] != inf;
}

int dfs(int u, int a) {
    if (u == _t || a == 0)
        return a;
    int flow = 0, f;
    for (int& i = cur[u]; i; i = e[i].nex) {
        int v = e[i].to;
        if (d[v] == d[u] + 1 && (f = dfs(v, min(e[i].f, a))) > 0) {
            e[i].f -= f;
            e[i ^ 1].f += f;
            flow += f;
            a -= f;
            if (!a)
                break;
        }
    }
    return flow;
}

int vis[2 * N + 2 * M];

void _dfs(int u) {
    if (vis[u])
        return;
    vis[u] = 1;
    for (int i = h[u]; i; i = e[i].nex) {
        if (e[i].f)
            _dfs(e[i].to);
    }
}

int main() {
    scanf("%d%d", &m, &c);
    _s = ++node_cnt;
    _t = ++node_cnt;
    for (int i = 1; i <= m; ++i) pos_f[i] = ++node_cnt;
    for (int i = 1; i <= c; ++i) pos_c[i] = ++node_cnt;
    scanf("%d", &n1);
    for (int i = 1, x, y; i <= n1; ++i) {
        scanf("%d%d", &x, &y);
        pos_a[i] = ++node_cnt;
        add_edge(_s, pos_a[i], 1);
        add_edge(pos_a[i], pos_f[x], 1);
        add_edge(pos_a[i], pos_c[y], 1);
    }
    scanf("%d", &n2);
    for (int i = 1, x, y; i <= n2; ++i) {
        scanf("%d%d", &x, &y);
        pos_b[i] = ++node_cnt;
        add_edge(pos_b[i], _t, 1);
        add_edge(pos_f[x], pos_b[i], 1);
        add_edge(pos_c[y], pos_b[i], 1);
    }
    while (bfs()) dfs(_s, inf);
    _dfs(_s);
    for (int i = 1; i <= n1; ++i) printf("%d\n", vis[pos_a[i]] ^ 1);
    return 0;
}