#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#define space putchar(' ')
#define enter putchar('\n')
typedef long long ll;
using namespace std;
template <class T>
void read(T &x){
    char c;
    bool op = 0;
    while(c = getchar(), c < '0' || c > '9')
        if(c == '-') op = 1;
    x = c - '0';
    while(c = getchar(), c >= '0' && c <= '9')
        x = x * 10 + c - '0';
    if(op) x = -x;
}
template <class T>
void write(T x){
    if(x < 0) putchar('-'), x = -x;
    if(x >= 10) write(x / 10);
    putchar('0' + x % 10);
}

const int N = 100005, W = 1000000021, P = 999999137;
int n, m, fa[N], f[N], g[N], pw[N], Sze[N], deg[N], ans = P;
int ecnt, adj[N], nxt[2*N], go[2*N];
vector <int> son[N], sl[N], sr[N];
set <int> vis;
bool isB;

void add(int u, int v){
    if(isB) deg[u]++;
    go[++ecnt] = v;
    nxt[ecnt] = adj[u];
    adj[u] = ecnt;
}
int dfs1(int u, int pre){
    Sze[u] = 1;
    fa[u] = pre;
    son[u].clear();
    for(int e = adj[u], v; e; e = nxt[e])
    if((v = go[e]) != pre){
        son[u].push_back(dfs1(v, u));
        Sze[u] += Sze[v];
    }
    if(son[u].empty()) return f[u] = 1;
    sort(son[u].begin(), son[u].end());
    ll ret = 0;
    for(int i = 0; i < (int)son[u].size(); i++)
    ret = (ret * W + son[u][i]) % P;
    return f[u] = Sze[u] * ret % P;
}

void dfs2(int u){
    if(fa[u]){
    son[u].push_back(g[u]);
    sort(son[u].begin(), son[u].end());
    }
    int sze = son[u].size();
    sl[u].resize(sze);
    sl[u][0] = son[u][0];
    for(int i = 1; i < sze; i++)
    sl[u][i] = ((ll)sl[u][i - 1] * W + son[u][i]) % P;
    sr[u].resize(sze);
    sr[u][sze - 1] = son[u][sze - 1];
    for(int i = sze - 2; i >= 0; i--)
    sr[u][i] = (sr[u][i + 1] + (ll)son[u][i] * pw[sze - i - 1]) % P;
    for(int e = adj[u], v; e; e = nxt[e])
    if((v = go[e]) != fa[u]){
        if(sze == 1){
        g[v] = 1;
        dfs2(v);
        break;
        }
        int p = lower_bound(son[u].begin(), son[u].end(), f[v]) - son[u].begin();
        g[v] = 0;
        if(p + 1 < sze) g[v] = sr[u][p + 1];
        if(p - 1 >= 0) g[v] = (g[v] + (ll)sl[u][p - 1] * pw[sze - 1 - p]) % P;
        g[v] = (ll)g[v] * (n - Sze[v]) % P;
        if(isB && deg[v] == 1 && vis.find(g[v]) != vis.end()) ans = min(ans, v);
        dfs2(v);
    }
    if(!isB) vis.insert((ll)sl[u][sze - 1] * n % P);
}

int main(){

    pw[0] = 1;
    for(int i = 1; i < N; i++)
    pw[i] = (ll)pw[i - 1] * W % P;
    read(n);
    for(int i = 1, u, v; i < n; i++)
    read(u), read(v), add(u, v), add(v, u);
    dfs1(1, 0);
    dfs2(1);
    ecnt = 0, isB = 1, n++;
    memset(adj, 0, sizeof(adj));
    for(int i = 1, u, v; i < n; i++)
    read(u), read(v), add(u, v), add(v, u);
    dfs1(1, 0);
    if(deg[1] == 1 && vis.find(f[go[adj[1]]]) != vis.end())
    ans = 1;
    dfs2(1);
    write(ans);

    return 0;
}