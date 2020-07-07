#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
#define re register
#define LL long long
#define MOD 998244353ll
#define MAXN 100005
using namespace std;
struct Node {
    int p, v;
    Node(int _ = 0, int __ = 0) { p = _, v = __; }
    bool friend operator<(const Node &x, const Node &y) { return x.v > y.v; }
};
struct Edge {
    int to, nex;
    LL w;
    Edge(int _ = 0, int __ = 0, LL ___ = 0) { to = _, nex = __, w = ___; }
} e[MAXN << 1];
LL n, m, k, cnt, st, ed, hd[MAXN], tp[MAXN], dis[MAXN][22];
bool vis[MAXN][22];
LL rd() {
    LL x = 0, tp = 1;
    char c;
    c = getchar();
    while (c < '0' || c > '9') {
        if (c == '-')
            tp = -1;
        c = getchar();
    }
    while (c >= '0' && c <= '9') {
        x = x * 10 + c - '0';
        c = getchar();
    }
    return x * tp;
}
void adde(int x, int y, LL z) {
    e[++cnt] = Edge(y, hd[x], z);
    hd[x] = cnt;
}
void dij() {
    memset(dis, INF, sizeof(dis));
    memset(vis, 0, sizeof(vis));
    priority_queue<Node> q;
    while (!q.empty()) q.pop();
    dis[st][tp[st] + 10] = 0;
    q.push(Node(st, tp[st] + 10));
    while (!q.empty()) {
        Node now = q.top();
        q.pop();
        while (!q.empty() && vis[now.p][now.v]) {
            now = q.top();
            q.pop();
            if (q.empty())
                return;
        }
        vis[now.p][now.v] = 1;
        for (int i = hd[now.p]; i; i = e[i].nex) {
            if (abs(now.v + tp[e[i].to] - 10) <= k &&
                dis[e[i].to][now.v + tp[e[i].to]] > dis[now.p][now.v] + e[i].w) {
                dis[e[i].to][now.v + tp[e[i].to]] = dis[now.p][now.v] + e[i].w;
                // printf("dis[%d][%d]=%lld\n",e[i].to,now.v+tp[e[i].to],dis[e[i].to][now.v+tp[e[i].to]]);
                q.push(Node(e[i].to, now.v + tp[e[i].to]));
            }
        }
    }
}
void smfa() {
    memset(dis, INF, sizeof(dis));
    memset(vis, 0, sizeof(vis));
    queue<Node> q;
    while (!q.empty()) q.pop();
    dis[st][tp[st] + 10] = 0;
    q.push(Node(st, tp[st] + 10));
    vis[st][tp[st] + 10] = 1;
    while (!q.empty()) {
        Node now = q.front();
        q.pop();
        vis[now.p][now.v] = 0;
        for (int i = hd[now.p]; i; i = e[i].nex) {
            if (abs(now.v + tp[e[i].to] - 10) <= k &&
                dis[e[i].to][now.v + tp[e[i].to]] > dis[now.p][now.v] + e[i].w) {
                dis[e[i].to][now.v + tp[e[i].to]] = dis[now.p][now.v] + e[i].w;
                // printf("dis[%d][%d]=%lld\n",e[i].to,now.v+tp[e[i].to],dis[e[i].to][now.v+tp[e[i].to]]);
                if (!vis[e[i].to][now.v + tp[e[i].to]])
                    q.push(Node(e[i].to, now.v + tp[e[i].to]));
            }
        }
    }
}
int main() {
    // freopen("testdata.in","r",stdin);
    // freopen("fake.out","w",stdout);
    int x, y, z, T = rd();
    while (T--) {
        cnt = 0;
        memset(hd, 0, sizeof(hd));
        n = rd(), m = rd(), k = rd();
        for (int i = 1; i <= n; i++) tp[i] = ((rd() == 1) ? 1 : -1);
        for (int i = 1; i <= m; i++) {
            x = rd(), y = rd(), z = rd();
            // for(int j=-k;j<=k;j++)
            adde(x, y, z), adde(y, x, z);
        }
        st = rd(), ed = rd();
        if (k == 0) {
            printf("-1\n");
            continue;
        }
        // dij();
        smfa();
        LL ans = INF;
        for (int i = 10 - k; i <= 10 + k; i++) ans = min(ans, dis[ed][i]);
        if (ans == INF)
            printf("-1\n");
        else
            printf("%lld\n", ans);
    }
    // printf("%.2lf\n",(double)clock()/CLOCKS_PER_SEC);
    return 0;
}