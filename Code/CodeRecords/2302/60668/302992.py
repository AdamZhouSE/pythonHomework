#include<bits/stdc++.h>
using namespace std;
inline int read(){
    int x=0;bool f=0;char ch;
    while(!isdigit(ch=getchar()))f|=ch=='-';
    while(isdigit(ch))x=(x<<1)+(x<<3)+(ch^48),ch=getchar();
    return f?-x:x;
}
inline void write(int x){
    if(x<0)putchar('-'),x=-x;
    if(x>9)write(x/10);
    putchar('0'+x%10);
}
const int N=100005;
int n,rot,q,cnt;
int head[N];
struct edge{int v,nxt;}e[N<<1];
inline void addedge(int u,int v){
    e[++cnt]=(edge){v,head[u]};head[u]=cnt;
}
int fa[N],siz[N],Hs[N],dep[N];
inline void dfs1(int u){
    siz[u]=1;dep[u]=dep[fa[u]]+1;
    for(int i=head[u];i;i=e[i].nxt){
        int v=e[i].v;
        dfs1(v);siz[u]+=siz[v];
        if(siz[v]>siz[Hs[u]])Hs[u]=v;
    }
}
int Lt[N];
inline void dfs2(int u){
    if(!Lt[u])Lt[u]=u;
    if(Hs[u])Lt[Hs[u]]=Lt[u],dfs2(Hs[u]);
    for(int i=head[u];i;i=e[i].nxt)
        if(e[i].v!=Hs[u])dfs2(e[i].v);
}
inline int Ask(int u,int v){
    while(Lt[u]!=Lt[v]){
        if(dep[Lt[u]]<dep[Lt[v]])swap(u,v);
        u=fa[Lt[u]];
    }
    if(dep[u]>dep[v])swap(u,v);
    return u;
}
int main(){
    n=read();rot=read();
    for(int i=1,f,ls,rs;i<=n;++i){
        f=read();ls=read();rs=read();
        if(ls)fa[ls]=f,addedge(f,ls);
        if(rs)fa[rs]=f,addedge(f,rs);
    }
    dfs1(rot);dfs2(rot);q=read();
    for(int i=1;i<=q;++i){
        write(Ask(read(),read()));
        putchar('\n');
    }
    return 0;
}