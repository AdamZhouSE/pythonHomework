#include<bits/stdc++.h>
#define fp(i,a,b) for(int i=(a),I=(b)+1;i<I;++i)
#define fd(i,a,b) for(int i=(a),I=(b)-1;i>I;--i)
#define go(G,u) for(int i=G.head[u],v=G.e[i].to;i;v=G.e[i=G.e[i].nxt].to)
#define ll long long
using namespace std;
const int inf=1e9+7;
const int M=3e4+3;
typedef int arr[M];
#ifndef Judge
#define getchar() (p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++)
#endif
char buf[1<<21],*p1=buf,*p2=buf;
inline bool cmax(int& a,int b){return a<b?a=b,1:0;}
inline bool cmin(int& a,int b){return a>b?a=b,1:0;}
inline int read(){ int x=0,f=1; char c=getchar();
    for(;!isdigit(c);c=getchar()) if(c=='-') f=-1;
    for(;isdigit(c);c=getchar()) x=x*10+c-'0'; return x*f;
} int n,m,k,root,tot,ans,num; arr in,dis,vis,siz,mx,cnt;
struct Gr{ int pat,head[M];
    struct Edge{ int to,val,nxt; }e[M<<2];
    inline void add(int u,int v,int w){
        e[++pat]={v,w,head[u]},head[u]=pat;
        e[++pat]={u,w,head[v]},head[v]=pat;
    }
}G,T;
struct node{ int dis,id;
    bool operator <(const node& b)const{
        return dis^b.dis?dis>b.dis:id>b.id;
    }
};
queue<node> q;
inline void dijkstra(){
    memset(dis,0x3f,n+2<<2);
    dis[1]=1,q.push({0,1});
    for(int u;!q.empty();){ u=q.front().id,in[u]=0,q.pop();
        go(G,u) if(cmin(dis[v],dis[u]+G.e[i].val))
            if(!in[v]) in[v]=1,q.push({dis[v],v});
    }
    fp(u,1,n) go(G,u)
        if(dis[v]==dis[u]+G.e[i].val&&!in[v])
            in[v]=1,T.add(u,v,G.e[i].val);
}
void get_root(int u,int fa){ mx[u]=0,siz[u]=1;
    go(T,u) if(!vis[v]&&v^fa) get_root(v,u),
        siz[u]+=siz[v],cmax(mx[u],siz[v]);
    cmax(mx[u],tot-siz[u]);
    if(mx[u]<mx[root]) root=u;
}
void clear(int u,int fa,int dep){
    cnt[dep+1]=0,dis[dep+1]=-inf;
    cnt[k-dep]=0,dis[k-dep]=-inf;
    go(T,u) if(!vis[v]&&v^fa)
        clear(v,u,dep+1);
}
void calc(int u,int fa,int dep,int ds){
    if(cmax(ans,ds+dis[k-dep]))
        num=cnt[k-dep];
    else if(ans==ds+dis[k-dep])
        num+=cnt[k-dep];
    go(T,u) if(!vis[v]&&v^fa)
        calc(v,u,dep+1,ds+T.e[i].val);
}
void dfs(int u,int fa,int dep,int ds){
    if(cmax(dis[dep+1],ds)) cnt[dep+1]=1;
    else if(dis[dep+1]==ds) ++cnt[dep+1];
    go(T,u) if(!vis[v]&&v^fa)
        dfs(v,u,dep+1,ds+T.e[i].val);
}
void solv(int u){
    get_root(u,0),u=root,vis[u]=1; 
    go(T,u) if(!vis[v]) clear(v,0,1); 
    dis[1]=0,cnt[1]=1;
    go(T,u) if(!vis[v]) 
        calc(v,0,1,T.e[i].val),
        dfs(v,0,1,T.e[i].val);
    go(T,u) if(!vis[v])
        tot=siz[v],root=0,solv(v);
}
int main(){ int x,y,z;
    n=read(),m=read(),k=read();
    fp(i,1,m) x=read(),y=read(),
        z=read(),G.add(x,y,z);
    dijkstra(),tot=mx[0]=n,solv(1);
    return !printf("%d %d\n",ans,num);
}