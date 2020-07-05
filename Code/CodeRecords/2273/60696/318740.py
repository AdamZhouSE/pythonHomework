// LOJ #2268
// DeP
#include <cctype>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

namespace IO {
const int MAXSIZE = 1 << 18 | 1;
char buf[MAXSIZE], *p1, *p2;

inline int Gc() {
    return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, MAXSIZE, stdin), p1 == p2) ? EOF : *p1++;
}
template <typename T>
inline void read(T& x) {
    x = 0;
    int f = 0, ch = Gc();
    while (!isdigit(ch)) f |= ch == '-', ch = Gc();
    while (isdigit(ch)) x = x * 10 + ch - '0', ch = Gc();
    if (f)
        x = -x;
}
}  // namespace IO
using IO::read;

const int MAXN = 2e4 + 5, MAXK = 5e5 + 5, MAXM = 2 * MAXK + 25e6 + 5;

int n, K, M, ans;
int pre[MAXN], A[MAXN], V[MAXN];
int f[MAXM], g[MAXM];

inline void solve(int* F, const int& a, const int& v) {
    static int Q[MAXK], W[MAXK], head, tail;
    Q[head = 1] = tail = 0;
    for (int i = 0, j = 0; i <= K; ++i, j += v) {
        F[i] -= j;
        while (head <= tail && F[Q[tail]] < F[i]) --tail;
        Q[++tail] = i;
        while (head <= tail && i - Q[head] > a) ++head;
        W[i] = F[Q[head]] + j;
    }
    memcpy(F, W, M * sizeof(int));
}

namespace Graph {
struct Edge {
    int nxt, to;
} edges[MAXN];
int head[MAXN], eidx;

inline void init() { memset(head, -1, (n + 1) * sizeof(int)), eidx = 1; }
inline void AddEdge(int from, int to) {
    edges[++eidx] = (Edge){ head[from], to };
    head[from] = eidx;
}

void dfs0(int u) {
    if (A[u])
        solve(f + M * u, A[u], V[u]);
    for (int i = head[u]; ~i; i = edges[i].nxt) {
        int v = edges[i].to;
        memcpy(f + M * v, f + M * u, M * sizeof(int));
        dfs0(v);
        for (int j = 1; j <= K; ++j) f[M * u + j] = max(f[M * u + j], f[M * v + j - 1] + V[v]);
    }
}

void dfs1(int u, int s) {
    for (int i = head[u]; ~i; i = edges[i].nxt) {
        int v = edges[i].to;
        memcpy(g + M * v, g + M * u, M * sizeof(int));
        dfs1(v, s + V[u]);
        for (int j = 1; j <= K; ++j) g[M * u + j] = max(g[M * u + j], g[M * v + j - 1] + V[v]);
    }
    if (head[u] == -1)  // leaf
        for (int j = 0; j <= K; ++j) ans = max(ans, V[u] + s + f[M * u + j] + g[M * u + K - j]);
    if (A[u])
        solve(g + M * u, A[u], V[u]);
}
}  // namespace Graph

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
#endif
    int Ti;
    read(Ti);
    while (Ti--) {
        // input
        read(n), read(K);
        for (int i = 1; i <= n; ++i) read(pre[i]), read(A[i]), read(V[i]), --A[i];
        // init
        ans = 0, M = K + 1;
        memset(f + M, 0, M * sizeof(int));
        memset(g + M, 0, M * sizeof(int));
        // solve
        Graph::init();
        for (int i = 2; i <= n; ++i) Graph::AddEdge(pre[i], i);
        Graph::dfs0(1);
        Graph::init();
        for (int i = n; i >= 2; --i) Graph::AddEdge(pre[i], i);
        Graph::dfs1(1, 0);
        // output
        printf("%d\n", ans);
    }
    return 0;
}