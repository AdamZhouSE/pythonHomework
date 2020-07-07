#include <bits/stdc++.h>
#define clear(a) memset(a, 0, sizeof a)
using namespace std;
const int N = 5e2 + 50;
struct node {
    int next, to;
} edge[N << 1];
int cnt, head[N];
inline void add(int from, int to) { edge[++cnt] = (node){ head[from], to }, head[from] = cnt; }
int low[N], dfn[N], visited[N], cut[N];
int tot, sky, size, num;
void tarjan(int u, int f) {
    low[u] = dfn[u] = ++tot;
    int child = 0;
    for (int i = head[u]; i; i = edge[i].next) {
        int v = edge[i].to;
        if (!dfn[v]) {
            tarjan(v, f), low[u] = min(low[u], low[v]);
            if (u == f)
                child++;
            if (u != f && low[v] >= dfn[u])
                cut[u] = 1;
        } else
            low[u] = min(low[u], dfn[v]);
    }
    if (u == f && child >= 2)
        cut[u] = 1;
}
void dfs(int u) {
    size++, visited[u] = sky;
    for (int i = head[u]; i; i = edge[i].next) {
        int v = edge[i].to;
        if (visited[v] != sky && cut[v])
            num++, visited[v] = sky;
        if (!visited[v] && !cut[v])
            dfs(v);
    }
}
int main() {
    int n = 0, m, t = 0;
    while (1) {
        clear(head), clear(edge), clear(cut);
        clear(visited), clear(low), clear(dfn);
        t++;
        n = cnt = tot = 0;
        scanf("%d", &m);
        if (m == 0)
            break;
        for (int i = 1; i <= m; i++) {
            int a, b;
            scanf("%d%d", &a, &b);
            add(a, b), add(b, a);
            n = max(max(a, b), n);
        }
        for (int i = 1; i <= n; i++)
            if (!dfn[i])
                tarjan(i, i);
        long long ans1 = 0, ans2 = 1;
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && !cut[i]) {
                num = size = 0, sky++, dfs(i);
                if (num == 0)
                    ans1 += 2, ans2 *= size * (size - 1) / 2;
                if (num == 1)
                    ans1++, ans2 *= size;
            }
        }
        printf("Case %d: %lld %lld\n", t, ans1, ans2);
    }
    return 0;
}