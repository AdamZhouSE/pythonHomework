#include <cstdio>
#include <cctype>
#include <cstring>

#include <algorithm>
#include <vector>

typedef long long LL;

inline char fgc() {
    static char buf[100000], *p1 = buf, *p2 = buf;
    return p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 100000, stdin), p1 == p2) ? EOF 
        : *p1++;
}

inline LL readint() {
    register LL res = 0, neg = 1;
    register char c = fgc();
    while(!isdigit(c)) {
        if(c == '-') neg = -1;
        c = fgc();
    }
    while(isdigit(c)) {
        res = (res << 1) + (res << 3) + c - '0';
        c = fgc();
    }
    return res * neg;
}

const int MAXN = 10005;

int n, m;

std::vector<int> gra[MAXN];

int dfn[MAXN], low[MAXN], clk;
bool cut[MAXN];

inline void tarjan(int u, int fa) {
    int ch = 0;
    dfn[u] = low[u] = ++clk;
    for(int i = 0; i < gra[u].size(); i++) {
        int v = gra[u][i];
        if(!dfn[v]) {
            ch++; tarjan(v, u);
            low[u] = std::min(low[u], low[v]);
            if(low[v] >= dfn[u]) cut[u] = true;
        } else if(dfn[v] < dfn[u] && v != fa) {
            low[u] = std::min(low[u], dfn[v]);
        }
    }
    if(ch == 1 && !fa) cut[u] = false;
}

int ccnt, siz, vis[MAXN], dclk;

inline void dfs(int u) {
    vis[u] = dclk; siz++;
    for(int i = 0; i < gra[u].size(); i++) {
        int v = gra[u][i];
        if(vis[v] != dclk && cut[v]) {
            ccnt++; vis[v] = dclk;
        }
        if(!vis[v] && !cut[v]) dfs(v);
    }
}

int u, v;

int main() {
    for(int kase = 1;; kase++) {
        memset(dfn, 0, sizeof(dfn));
        memset(low, 0, sizeof(low));
        memset(cut, 0, sizeof(cut));
        memset(vis, 0, sizeof(vis));
        n = clk = dclk = 0;
        m = readint(); if(!m) break;
        for(int i = 1; i < MAXN; i++) gra[i].clear();
        for(int i = 1; i <= m; i++) {
            u = readint(); v = readint();
            gra[u].push_back(v);
            gra[v].push_back(u);
            n = std::max(n, std::max(u, v));
        }
        for(int i = 1; i <= n; i++) {
            if(!dfn[i]) tarjan(i, 0);
        }
        int ans1 = 0;
        LL ans2 = 1;
        for(int i = 1; i <= n; i++) {
            if(!vis[i] && !cut[i]) {
                dclk++; ccnt = siz = 0;
                dfs(i);
                if(!ccnt) {
                    ans1 += 2;
                    ans2 *= 1ll * siz * (siz - 1) / 2;
                } else if(ccnt == 1) {
                    ans1++;
                    ans2 *= siz;
                }
            }
        }
        printf("Case %d: %d %lld\n", kase, ans1, ans2);
    }
    return 0;
}