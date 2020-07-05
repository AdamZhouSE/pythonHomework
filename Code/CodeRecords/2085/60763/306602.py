#include <cstdio>

using namespace std;

typedef long long ll;

const int maxn=1e2+50;
const int maxm=1e4+50;
const int inf=0x3f3f3f3f;

int n,m,r;
ll ans;

inline int read() {
    int a=0;char c=getchar();
    while(c<'0'||c>'9') c=getchar();
    while(c>='0'&&c<='9') a=(a<<1)+(a<<3)+c-'0',c=getchar();
    return a;
}

struct edge {int u,v,w;}e[maxm];

int cnt,fa[maxn],id[maxn],top[maxn],min[maxn];
//cnt当前图环的数量 
//id[u]代表u节点在第id[u]个环中
//top[u]代表u所在链的代表元素 类似并查集 
//min[u]为当前连到u点的最短边的边权 fa[v]当前连到v点的最短边的u 

inline int getans() {
    while(1) {
        for(register int i=1;i<=n;++i) id[i]=top[i]=0,min[i]=inf;
        for(register int i=1;i<=m;++i)
            if(e[i].u!=e[i].v&&e[i].w<min[e[i].v])
            //不是自环 并且边权比选定的还小 
                fa[e[i].v]=e[i].u,min[e[i].v]=e[i].w;
        int u=min[r]=0;
        for(register int i=1;i<=n;++i) {
            if(min[i]==inf) return 0; //存在一个不可以连接的点 
            ans+=min[i];
            for(u=i;u!=r&&top[u]!=i&&!id[u];u=fa[u]) top[u]=i;
            //找到包含不在环中的点最多的链 打上标记 
            if(u!=r&&!id[u]) { //这时候还满足条件说明vis[u]==i 即成环 
                id[u]=++cnt;
                for(int v=fa[u];v!=u;v=fa[v]) id[v]=cnt;
            }
        }if(!cnt) return 1; //没环就是找到答案了 
        for(register int i=1;i<=n;++i) if(!id[i]) id[i]=++cnt;
        //i节点不存在当前树中 就给他自己成一个环 
        for(register int i=1;i<=m;++i) {
            int last=min[e[i].v];
            //last等于当前连进v点的边的最小权值 
            if((e[i].u=id[e[i].u])!=(e[i].v=id[e[i].v])) e[i].w-=last;
            //当前边的两个端点不在同一个环内 
        }n=cnt;r=id[r];cnt=0;
        //缩完点后 当前点数就为环数 根节点就是根节点所在的环 
    }
}

int main() {
    n=read();m=read();r=read();
    for(register int i=0;i<m;e[++i]=(edge){read(),read(),read()});
    if(getans()) printf("%lld",ans);
    else printf("-1");
    return 0;
}