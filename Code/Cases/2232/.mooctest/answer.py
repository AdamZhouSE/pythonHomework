#include <bits/stdc++.h>
using namespace std;
const int MAXN = 110;
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
int outdeg[MAXN];
int stk[MAXN];
int stkTop;
int flag[MAXN][MAXN];
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
    // freopen("test.in", "r", stdin);
    init();
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        int v;
        while (~scanf("%d", &v)) {
            if (!v) {
                break;
            }
            addEdge(i, v);
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
            int u = belong[i], v = belong[next];
            if (u != v && !flag[u][v]) {
                flag[u][v] = 1;
                outdeg[u]++;
                indeg[v]++;
            }
        }
    }
    int ans1 = 0;
    for (int i = 1; i <= scc; i++) {
        if (!indeg[i]) {
            ans1++;
        }
    }
    int ans2 = 0, cnt1 = 0, cnt2 = 0;
    for (int i = 1; i <= scc; i++) {
        if (!indeg[i]) {
            cnt1++;
        }
        if (!outdeg[i]) {
            cnt2++;
        }
    }
    if (scc == 1) {
        ans2 = 0;
    } else {
        ans2 = max(cnt1, cnt2);
    }
    printf("%d\n", ans1);
    printf("%d\n", ans2);
    return 0;
}