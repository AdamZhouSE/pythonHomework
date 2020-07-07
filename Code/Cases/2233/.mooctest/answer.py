#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e3 + 10;
int n;
int ecnt;
int head[MAXN];
struct Edge {
    int next, to;
} e[MAXN * MAXN];
int scc;
int dfn[MAXN];
int low[MAXN];
int inS[MAXN];
int belong[MAXN];
int indeg[MAXN];
int stk[MAXN];
int stkTop;
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
        } while (top != now);
    }
}
int main() {
    //  freopen("test.in", "r", stdin);
    init();
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int v;
            scanf("%d", &v);
            if (v) {
                addEdge(i, j);
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        if (!dfn[i]) {
            tarjan(i);
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = head[i]; ~j; j = e[j].next) {
            int next = e[j].to;
            if (belong[i] != belong[next]) {
                indeg[belong[next]]++;
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= scc; i++) {
        if (!indeg[i]) {
            ans++;
        }
    }
    printf("%d\n", ans);
    return 0;
}