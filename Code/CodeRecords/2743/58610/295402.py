#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LL long long int
#define REP(i,n) for (int i = 1; i <= (n); i++)
#define Redge(u) for (int k = h[u],to; k; k = ed[k].nxt)
#define BUG(s,n) for (int i = 1; i <= (n); i++) cout<<s[i]<<' '; puts("");
using namespace std;
const int maxn = 300005,maxm = 600005,INF = 1000000000;
inline int RD(){
    int out = 0,flag = 1; char c = getchar();
    while (c < 48 || c > 57) {if (c == '-') flag = -1; c = getchar();}
    while (c >= 48 && c <= 57) {out = (out << 3) + (out << 1) + c - '0'; c = getchar();}
    return out * flag;
}
int n,fa[maxn][20],A[maxn],dep[maxn],C[maxn];
int h[maxn],ne = 2;
struct EDGE{int to,nxt;}ed[maxm];
inline void build(int u,int v){
    ed[ne] = (EDGE){v,h[u]}; h[u] = ne++;
    ed[ne] = (EDGE){u,h[v]}; h[v] = ne++;
}
void dfs(int u){
    REP(i,19) fa[u][i] = fa[fa[u][i - 1]][i - 1];
    Redge(u) if ((to = ed[k].to) != fa[u][0]){
        fa[to][0] = u; dep[to] = dep[u] + 1;
        dfs(to);
    }
}
int Lca(int u,int v){
    if (dep[u] < dep[v]) swap(u,v);
    int d = dep[u] - dep[v];
    for (int i = 0; (1 << i) <= d; i++)
        if ((1 << i) & d) u = fa[u][i];
    if (u == v) return u;
    for (int i = 19; i >= 0; i--)
        if (fa[u][i] != fa[v][i]) u = fa[u][i],v = fa[v][i];
    return fa[u][0];
}
void dfs1(int u){
    Redge(u) if ((to = ed[k].to) != fa[u][0])
        dfs1(to),C[u] += C[to];
}
int main(){
    n = RD(); int u,v,lca;
    REP(i,n) A[i] = RD();
    REP(i,n - 1) build(RD(),RD());
    dfs(dep[1] = 1);
    for (int i = 1; i < n; i++){
        u = A[i]; v = A[i + 1]; lca = Lca(u,v);
        C[u]++,C[fa[v][0]]++,C[lca]--,C[fa[lca][0]]--;
    }
    dfs1(1);
    REP(i,n) printf("%d\n",C[i]);
    return 0;
}