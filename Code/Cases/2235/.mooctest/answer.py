#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1e5 + 10;
const int MAXM = 1e6 + 10;
int n, m;
int ecnt;
int head[MAXN];
struct Edge {
    int next, to;
} e[MAXM];
void init() {
    ecnt = 0;
    memset(head, -1, sizeof(head));
}
void addEdge(int x, int y) {
    e[ecnt].next = head[x];
    e[ecnt].to = y;
    head[x] = ecnt++;
}
struct _2SAT {
    int mark[MAXN];
    int stkTop;
    int stk[MAXN];
    void init() {
        stkTop = 0;
        memset(mark, 0, sizeof(mark));
    }
    void clear() {
        while (stkTop > 0) {
            mark[stk[stkTop--]] = 0;
        }
    }
    bool DFS(int now) {
        if (mark[now ^ 1]) {
            return 0;
        }
        if (mark[now]) {
            return 1;
        }
        mark[now] = 1;
        stk[++stkTop] = now;
        for (int i = head[now]; ~i; i = e[i].next) {
            int next = e[i].to;
            if (!DFS(next)) {
                return 0;
            }
        }
        return 1;
    }
    bool solve() {
        for (int i = 0; i < 2 * n; i += 2) {
            if (!mark[i] && !mark[i ^ 1]) {
                stkTop = 0;
                if (!DFS(i)) {
                    clear();
                    if (!DFS(i ^ 1)) {
                        return 0;
                    }
                }
            }
        }
        return 1;
    }
    void print() {
        for (int i = 0; i < 2 * n; i++) {
            if (mark[i]) {
                printf("%d\n", i + 1);  //默认从1开始编号
            }
        }
    }
} sat;
int main() {
    //  freopen("test.in", "r", stdin);
    init();
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--, v--;
        addEdge(u, v ^ 1);
        addEdge(v, u ^ 1);
    }
    sat.init();
    if (!sat.solve()) {
        printf("NIE\n");
    } else {
        sat.print();
    }
    return 0;
}