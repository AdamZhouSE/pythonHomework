
#include <bits/stdc++.h>
using namespace std;
const  int maxn=3e5+100;
#define INF 0x3f3f3f;
const int mod=998244353;
typedef  long long ll;
ll val[maxn][60];
int nextt[maxn<<1];
int head[maxn<<1];
int s[maxn<<1];
int cnt = 0;
int fa[maxn][50];
ll dep[maxn<<1];
ll c[100];
bool vis[maxn<<1];
 
void add(int u,int v)
{
    s[++cnt] = v;
    nextt[cnt] = head[u];
    head[u] = cnt;
    //cnt++;
}
 
void dfs(int u)
{
    vis[u] = 1;
    for(int i=0; fa[u][i]; i++){
        fa[u][i+1] = fa[fa[u][i]][i];
    }
    for(int i=head[u]; i; i=nextt[i]){
        int v = s[i];
        if(vis[v])  continue;
        dep[v] = dep[u] + 1;
        fa[v][0] = u;
        for(int j=1; j<=50; j++){
            c[j] = c[j-1] * dep[v] % mod;
        }
        for(int j=1; j<=50; j++){
            val[v][j] = (c[j] + val[u][j]) % mod;
        }
        dfs(v);
    }
}
 
int lca(int u,int v)
{
    if(dep[u] < dep[v])
        swap(u,v);
    int d = dep[u] - dep[v];
    for(int i=0; d; i++){
        if(d & 1){
            u = fa[u][i];
        }
        d >>= 1;
    }
    if(u == v)
        return u;
    for(int i=20; i>=0; i--){
        if(fa[u][i] != fa[v][i]){
            u = fa[u][i];
            v = fa[v][i];
        }
    }
    return fa[u][0];
}
int main()
{
    int n;
    scanf("%d",&n);
    int u,v;
    c[0] = 1;
    for(int i=1; i<n; i++){
        scanf("%d%d",&u,&v);
        add(u,v);
        add(v,u);
    }
    dfs(1);
    int m,w;
    scanf("%d",&m);
    while(m--){
        scanf("%d%d%d",&u,&v,&w);
        int l = lca(u,v);
        ll ans = (val[u][w] + val[v][w] - val[fa[l][0]][w] + mod - val[l][w] + mod) % mod;
        printf("%lld\n",ans);
    }
    return 0;
}