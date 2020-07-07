#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAXN = 3e3 + 10;
int n, p, r;
int v[MAXN];
int ecnt;
int head[MAXN];
struct Edge {
    int next, to;
} e[MAXN * MAXN];
int scc;
int dfn[MAXN];
int low[MAXN];
int inS[MAXN];
int stkTop;
int stk[MAXN];
int belong[MAXN];
int indeg[MAXN];
int value[MAXN];
int vis[MAXN];
void init() {
    ecnt = 0;
    memset(head, -1, sizeof(head));
}
void addEdge(int x, int y) {
    e[ecnt].next = head[x];
    e[ecnt].to = y;
    head[x] = ecnt++;
}
void tarjan(int now) {
    low[now] = dfn[now] = ++stkTop;
    stk[stkTop] = now;
    inS[now] = 1;
    for (int i = head[now]; ~i; i = e[i].next) {
        int next = e[i].to;
        if (!dfn[next]) {
            tarjan(next);
            low[now] = min(low[now], low[next]);
        } else if (inS[next]) {
            low[now] = min(low[now], dfn[next]);
        }
    }
    if (low[now] == dfn[now]) {
        scc++;
        int top;
        do {
            top = stk[stkTop--];
            inS[top] = 0;
            belong[top] = scc;
            value[scc] = min(value[scc], v[top]);
        } while (top != now);
    }
}
void DFS(int now) {
    vis[now] = 1;
    for (int i = head[now]; ~i; i = e[i].next) {
        int next = e[i].to;
        if (!vis[next]) {
            DFS(next);
        }
    }
}
int main() {
    // freopen("test.in", "r", stdin);
    init();
    scanf("%d %d", &n, &p);
    for (int i = 1; i <= n; i++) {
        v[i] = value[i] = INF;
    }
    for (int i = 1; i <= p; i++) {
        int id, cost;
        scanf("%d %d", &id, &cost);
        v[id] = cost;
    }
    scanf("%d", &r);
    for (int i = 1; i <= r; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        addEdge(u, v);
    }
    for (int i = 1; i <= n; i++) {
        if (!vis[i] && v[i] != INF) {
            DFS(i);
        }
    }
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            printf("NO\n");
            printf("%d\n", i);
            return 0;
        }
    }
    for (int i = 1; i <= n; i++) {
        if (!dfn[i]) {
            tarjan(i);
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = head[i]; ~j; j = e[j].next) {
            int u = belong[i], v = belong[e[j].to];
            if (u != v) {
                indeg[v]++;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= scc; i++) {
        if (!indeg[i]) {
            ans += value[i];
        }
    }
    printf("YES\n");
    printf("%d\n", ans);
    return 0;
}