#include <bits/stdc++.h>
#define fi first
#define se second
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define enter putchar('\n')
#define space putchar(' ')
#define MAXN 20005
#define eps 1e-8
//#define ivorysi
using namespace std;
typedef long long int64;
typedef double db;
template<class T>
void read(T &res) {
    res = 0;char c = getchar();T f = 1;
    while(c < '0' || c > '9') {
    if(c == '-') f = -1;
    c = getchar();
    }
    while(c >= '0' && c <= '9') {
    res = res * 10 + c - '0';
    c = getchar();
    }
    res *= f;
}
template<class T>
void out(T x) {
    if(x < 0) {x = -x;putchar('-');}
    if(x >= 10) {
    out(x / 10);
    }
    putchar('0' + x % 10);
}
struct node {
    int to,next;
}E[MAXN * 2];
int N,M,head[MAXN],sumE,col[MAXN];
int dfn[MAXN],low[MAXN],idx,sta[MAXN],top,cnt,Ecnt,Ncnt,tot;
int vis[MAXN],tims,deg[MAXN],path[5],pc;
vector<int> ver[MAXN];
void add(int u,int v) {
    E[++sumE].to = v;
    E[sumE].next = head[u];
    head[u] = sumE;
}
void Init() {
    read(N);read(M);
    sumE = 0;memset(head,0,sizeof(head));
    memset(col,0,sizeof(col));memset(vis,0,sizeof(vis));tims = 0;
    memset(dfn,0,sizeof(dfn));memset(low,0,sizeof(low));idx = 0;
    int u,v;
    for(int i = 1 ; i <= M ; ++i) {
    read(u);read(v);
    add(u,v);add(v,u);
    }
}
bool color(int u) {
    if(!col[u]) col[u] = 2;
    for(int i = head[u] ; i ; i = E[i].next) {
    int v = E[i].to;
    if(!col[v]) {
        col[v] = col[u] ^ 1;
        if(!color(v)) return false;
    }
    else if(col[v] == col[u]) return false;
    }
    return true;
}
void Tarjan(int u) {
    dfn[u] = low[u] = ++idx;
    sta[++top] = u;
    ++Ncnt;
    for(int i = head[u] ; i ; i = E[i].next) {
    ++Ecnt;
    int v = E[i].to;
    if(dfn[v]) {low[u] = min(low[u],dfn[v]);}
    else {
        Tarjan(v);
        if(low[v] >= dfn[u]) {
        int t = 1;
        ++tot;ver[tot].clear();ver[tot].pb(u);
        while(1) {
            int x = sta[top--];
            ++t;
            ver[tot].pb(x);
            if(x == v) break;
        }
        if(t >= 4) ++cnt;
        }
        low[u] = min(low[u],low[v]);
    }
    }
}
void dfs_path(int u,int fa,int ed,int dep) {
    if(u == ed) {path[++pc] = dep;return;}
    for(int i = head[u] ; i ; i = E[i].next) {
    int v = E[i].to;
    if(vis[v] == tims && v != fa) {
        dfs_path(v,u,ed,dep + 1);
    }
    }
}
void Solve() {
    for(int i = 1 ; i <= N ; ++i) {
    if(!col[i]) {
        if(!color(i)) {puts("NO");return;}
    }
    } 
    
    for(int i = 1 ; i <= N ; ++i) {
    if(!dfn[i]) {
        top = 0;cnt = 0;Ecnt = 0;Ncnt = 0;tot = 0;
        Tarjan(i);
        Ecnt /= 2;
        if(Ecnt <= Ncnt) continue;
        if(Ecnt >= Ncnt + 2) {puts("NO");return;}
        if(cnt >= 2) {puts("NO");return;}
        ++tims;
        int st,ed;
        for(int j = 1 ; j <= tot;  ++j) {
        if(ver[j].size() >= 4) {
            for(int k = 0 ; k < ver[j].size() ; ++k) {
            vis[ver[j][k]] = tims;
            deg[ver[j][k]] = 0;
            }
            for(int k = 0 ; k < ver[j].size() ; ++k) {
            int u = ver[j][k];
            for(int h = head[u] ; h ; h = E[h].next) {
                int v = E[h].to;
                if(vis[v] == tims) {
                ++deg[u];
                }
            }
            }
            st = 0;ed = 0;
            for(int k = 0 ; k < ver[j].size() ; ++k) {
            int u = ver[j][k];
            if(deg[u] == 3) {
                if(!st) st = u;
                else if(!ed) ed = u; 
            }
            }
            break;
        }
        }
        pc = 0;
        dfs_path(st,0,ed,0);
        sort(path + 1,path + pc + 1);
        if(path[1] == 2 && path[2] == 2) continue;
        else {puts("NO");return;}
    }
    }
    puts("YES");
}
int main() {
#ifdef ivorysi
    freopen("f1.in","r",stdin);
#endif
    int T;
    read(T);
    while(T--) {
    Init();
    Solve();
    }
    return 0;
}