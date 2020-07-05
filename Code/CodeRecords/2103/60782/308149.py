#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MX = 300005;
const int MOD = 998244353;
int n, x, y, Q, ans[MX], f[MX], deep[MX], que[MX], h, t;
int bz[MX], head[MX], tot, headQ[MX], totQ;
int biao[300001][51];
bool vis[MX];
struct node {
    int v, w, nxt;
} e[MX << 1], q[MX << 1];
struct data {
    int u, v, w;
} query[MX];

int Find(int x) {
    return f[x] == x ? x : (f[x] = Find(f[x]));
}

void addEdge(int u, int v) {
    tot++;
    e[tot].v = v;
    e[tot].nxt = head[u];
    head[u] = tot;
    tot++;
    e[tot].v = u;
    e[tot].nxt = head[v];
    head[v] = tot;
}

void addEdge2(int u, int v, int w) {
    totQ++;
    q[totQ].v = v;
    q[totQ].w = w;
    q[totQ].nxt = headQ[u];
    headQ[u] = totQ;
    totQ++;
    q[totQ].v = u;
    q[totQ].w = w;
    q[totQ].nxt = headQ[v];
    headQ[v] = totQ;
}

void work(int x) {
    bz[x] = 1;
    for (int k = head[x]; k; k = e[k].nxt)
        if (!bz[e[k].v]) {
            work(e[k].v), f[e[k].v] = x;
        }

    for (int k = headQ[x]; k; k = q[k].nxt)
        if (bz[q[k].v])
            ans[q[k].w] = Find(q[k].v);
}

int Ans(int I) {
    int a = deep[ans[I]];
    int b = deep[query[I].u];
    int c = deep[query[I].v];
    int w = query[I].w;
    int res;
    if (b > c) swap(b, c);
    if (a==0) res = biao[b][w];
    else res=(biao[b][w]-biao[a-1][w]+MOD)%MOD;
    res=(res+biao[c][w])%MOD;
    res=(res-biao[a][w]+MOD)%MOD;
    return res;
}

int main() {
    //freopen("../in", "r", stdin);
    for (int i = 1; i <= 300000; ++i) {
        biao[i][0] = 1;
        for (int j = 1; j <= 50; ++j)
            biao[i][j] = 1ll * biao[i][j - 1] * i % MOD;
    }
    for (int i=1;i<=50;++i)
        for (int j=1;j<=300000;++j)
            biao[j][i] = (biao[j - 1][i] + biao[j][i]) % MOD;

    scanf("%d", &n);
    for (int i = 1; i < n; ++i) {
        scanf("%d%d", &x, &y);
        addEdge(x, y);
    }
    deep[1] = 0;
    h = t = -1;
    que[++t] = 1;
    vis[1] = true;
    while (h < t) {
        x = que[++h];
        for (int i = head[x]; i; i = e[i].nxt) {
            y = e[i].v;
            if (vis[y]) continue;
            vis[y] = true;
            deep[y] = deep[x] + 1;
            que[++t] = y;
        }
    }
    //for (int i=1;i<=n;++i) printf("%d %d\n",i,deep[i]);
    scanf("%d", &Q);
    for (int i = 0; i < Q; ++i) {
        scanf("%d%d%d", &x, &y, &t);
        addEdge2(x, y, i);
        query[i].u = x;
        query[i].v = y;
        query[i].w = t;
    }
    for (int i = 1; i <= n; ++i) f[i] = i;

    work(1);
    for (int i = 0; i < Q; ++i) printf("%d\n", Ans(i));
}