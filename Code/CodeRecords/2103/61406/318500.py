#include<iostream>
#include<cstring>
#include<cstdio>
#define maxn 300001
#define maxk 51
#define p 998244353
using namespace std;

struct edge{
    int to,next;
    edge(){}
    edge(const int &_to,const int &_next){ to=_to,next=_next; }
}e[maxn<<1];
int head[maxn],k;

long long dep[maxn],idep[maxn][maxk],val[maxn][maxk];
int size[maxn],fa[maxn],son[maxn],top[maxn];
int n,m;

inline int read(){
    register int x(0),f(1); register char c(getchar());
    while(c<'0'||'9'<c){ if(c=='-') f=-1; c=getchar(); }
    while('0'<=c&&c<='9') x=(x<<1)+(x<<3)+(c^48),c=getchar();
    return x*f;
}
inline void add(const int &u,const int &v){
    e[k]=edge(v,head[u]);
    head[u]=k++;
}

void dfs_getson(int u){
    size[u]=1;
    for(register int i=head[u];~i;i=e[i].next){
        int v=e[i].to;
        if(v==fa[u]) continue;
        dep[v]=dep[u]+1,fa[v]=u;
        idep[v][0]=1;
        for(register int j=1;j<maxk;j++) idep[v][j]=idep[v][j-1]*dep[v]%p;
        for(register int j=1;j<maxk;j++) val[v][j]=(val[u][j]+idep[v][j])%p;
        dfs_getson(v);
        size[u]+=size[v];
        if(size[v]>size[son[u]]) son[u]=v;
    }
}
void dfs_rewrite(int u,int tp){
    top[u]=tp;
    if(son[u]) dfs_rewrite(son[u],tp);
    for(register int i=head[u];~i;i=e[i].next){
        int v=e[i].to;
        if(v!=son[u]&&v!=fa[u]) dfs_rewrite(v,v);
    }
}

inline int lca(int u,int v){
    while(top[u]!=top[v]){
        if(dep[top[u]]>dep[top[v]]) swap(u,v);
        v=fa[top[v]];
    }
    if(dep[u]>dep[v]) swap(u,v);
    return u;
}

int main(){
    memset(head,-1,sizeof head);
    n=read();
    for(register int i=1;i<n;i++){
        int u=read(),v=read();
        add(u,v),add(v,u);
    }
    dfs_getson(1);
    dfs_rewrite(1,1);
    
    m=read();
    while(m--){
        int u=read(),v=read(),t=read();
        int w=lca(u,v);
        printf("%lld\n",(val[u][t]+val[v][t]+(p<<1)-val[w][t]-val[fa[w]][t])%p);
    }
    return 0;
}