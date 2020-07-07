#include <bits/stdc++.h>
int n, m;
int S = 1, T = 2;
int cur[6000];
int deep[3000];
char a[501][501];
int head[6000], tot = 1;
int rbelone[111][111], rt;
int cbelone[111][111], ct;
std::queue<int> q;
struct edge {
    int to;
    int nxt;
    int flow;
} e[1000000];
void add(int x, int y, int flow) {
    e[++tot] = { y, head[x], flow };
    head[x] = tot;
    e[++tot] = { x, head[y], 0 };
    head[y] = tot;
}
bool bfs() {
    memset(deep, 0, sizeof deep);
    deep[S] = 1;
    q.push(S);
    while (!q.empty()) {
        int X = q.front();
        q.pop();
        for (int i = head[X]; i; i = e[i].nxt) {
            int y = e[i].to;
            if (!deep[y] && e[i].flow) {
                deep[y] = deep[X] + 1;
                q.push(y);
            }
        }
    }
    return deep[T];
}
int dfs(int x, int flow) {
    if (x == T || !flow)
        return flow;
    int Flow = 0;
    for (int &i = cur[x]; i; i = e[i].nxt) {
        int y = e[i].to;
        if (e[i].flow && deep[y] == deep[x] + 1) {
            int w = dfs(y, std::min(flow, e[i].flow));
            if (w) {
                e[i].flow -= w;
                e[i ^ 1].flow += w;
                Flow += w;
                flow -= w;
                if (!flow)
                    break;
            }
        }
    }
    return Flow;
}
int dinic() {
    int maxflow = 0;
    while (bfs()) {
        memcpy(cur, head, sizeof head);
        for (;;) {
            int w = dfs(S, 0x3f3f3f3f);
            if (!w)
                break;
            maxflow += w;
        }
    }
    return maxflow;
}
main() {
    scanf("%d%d", &n, &m);
    getchar();
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) a[i][j] = getchar();
        if (i != n)
            getchar();
    }
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (a[i][j] != '#')
                rbelone[i][j] = (a[i][j - 1] != '#' && j > 1) ? rt : ++rt;
    for (int j = 1; j <= m; ++j)
        for (int i = 1; i <= n; ++i)
            if (a[i][j] != '#')
                cbelone[i][j] = (a[i - 1][j] != '#' && i > 1) ? ct : ++ct;
    for (int i = 1; i <= rt; ++i) add(S, 2 + i, 1);
    for (int i = 1; i <= ct; ++i) add(2 + rt + i, T, 1);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (a[i][j] == '*')
                add(2 + rbelone[i][j], 2 + rt + cbelone[i][j], 1);
    printf("%d", dinic());
    return 0;
}