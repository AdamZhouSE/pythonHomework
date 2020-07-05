#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = (a); i <= (b); i++)
#define per(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;
const int INF = 0x3f3f3f3f;
const int N = 500010;
int ans, n, m, idx, s, t;
string st[N];
int cnt = 1, hed[N], to[N], nxt[N], val[N], cur[N];
int dep[N];
queue<int> q;

int Id(int x, int y) { return x * m + y + 1; }
inline void add(int x, int y, int w) {
    to[++cnt] = y, nxt[cnt] = hed[x], hed[x] = cnt, val[cnt] = w;
    to[++cnt] = x, nxt[cnt] = hed[y], hed[y] = cnt, val[cnt] = 0;
}
bool bfs() {
    rep(i, s, t) dep[i] = 0;
    dep[s] = 1, q.push(s);
    for (int u; !q.empty();) {
        u = q.front(), q.pop();
        for (int i = hed[u]; i; i = nxt[i])
            if (!dep[to[i]] && val[i])
                dep[to[i]] = dep[u] + 1, q.push(to[i]);
    }
    return dep[t];
}
int dfs(int u, int w) {
    if (u == t)
        return w;
    for (int i = cur[u], ii = i;;) {
        if (dep[to[i]] != dep[u] + 1 || !val[i]) {
            i = nxt[i];
            if (!i)
                i = hed[u];
            if (i == ii)
                break;
            continue;
        }
        int flow = dfs(to[i], min(w, val[i]));
        if (flow) {
            cur[u] = i, val[i] -= flow, val[i ^ 1] += flow;
            return flow;
        }
        i = nxt[i];
        if (!i)
            i = hed[u];
        if (i == ii)
            break;
    }
    return 0;
}
int Dinic() {
    int res = 0;
    rep(i, s, t) cur[i] = hed[i];
    for (; bfs();)
        for (int tmp = dfs(s, INF); tmp; tmp = dfs(s, INF)) res += tmp;
    return res;
}
int main() {
    ios::sync_with_stdio(0);
    cin >> n >> m, s = 0, t = n * m + 1;
    rep(i, 0, n - 1) {
        cin >> st[i];
        rep(j, 0, m - 1) if (st[i][j] == '2')++ ans;
    }
    rep(i, 0, n - 1) rep(j, 0, m - 1) if (st[i][j] != '2' && st[i][j] != '*') {
        int x, y;
        x = i + 1, y = j;
        if (x < n && st[x][y] != '*' && (st[i][j] - '0') * (st[x][y] - '0') == 3) {
            if (st[i][j] == '1')
                add(Id(i, j), Id(x, y), 1);
            else
                add(Id(x, y), Id(i, j), 1);
        }
        x = i, y = j + 1;
        if (y < m && st[x][y] != '*' && (st[i][j] - '0') * (st[x][y] - '0') == 3) {
            if (st[i][j] == '1')
                add(Id(i, j), Id(x, y), 1);
            else
                add(Id(x, y), Id(i, j), 1);
        }
        if (st[i][j] == '1')
            add(s, Id(i, j), 1);
        else
            add(Id(i, j), t, 1);
    }
    printf("%d\n", ans + Dinic());
    return 0;
}