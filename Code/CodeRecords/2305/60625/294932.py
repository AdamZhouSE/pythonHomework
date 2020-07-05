#include<bits/stdc++.h>
using namespace std;
#define Set(a,b) memset(a,b,sizeof(a))
template<class T>inline void init(T&x){
    x=0;char ch=getchar();bool t=0;
    for(;ch>'9'||ch<'0';ch=getchar()) if(ch=='-') t=1;
    for(;ch>='0'&&ch<='9';ch=getchar()) x=(x<<1)+(x<<3)+(ch-48);
    if(t) x=-x;return;
}typedef long long ll;
const int N=4e4+10;
const int MAXN=2e5+10;
const int MAXM=2e6+10;
int m,c,n1,n2;
struct edge{
    int to,next,cap;
}a[MAXM<<2];
int head[MAXN],cnt=0,cur[MAXN],d[MAXN];
inline void add(int x,int y,int z){a[cnt]=(edge){y,head[x],z};head[x]=cnt++;}
inline void add_edge(int x,int y,int z){add(x,y,z),add(y,x,0);}
int X1[N],X2[N],Y1[N],Y2[N];
int idnum[N],idcol[N],idshi[N];
int S=0,T;
queue<int> Q;
int dfs(int u,int flow){
    if(u==T) return flow;
    int res=flow;
    for(int v,&i=cur[u];~i;i=a[i].next) {
        v=a[i].to;if(!a[i].cap||d[v]!=d[u]+1) continue;
        int f=dfs(v,min(res,a[i].cap));
        a[i].cap-=f,a[i^1].cap+=f;
        res-=f;if(!f) d[v]=0;
        if(!res) break;
    }
    return flow-res;
}
inline bool bfs(){
    for(int i=S;i<=T;++i) d[i]=0;d[S]=1;
    while(!Q.empty()) Q.pop();Q.push(S);
    while(!Q.empty()) {
        int u=Q.front();Q.pop();
        for(int v,i=head[u];~i;i=a[i].next) {
            v=a[i].to;if(!a[i].cap||d[v]) continue;
            d[v]=d[u]+1;if(v==T) return 1;Q.push(v);
        }
    }
    return d[T];
}
inline void Dinic(){
    int fl=0;
    while(bfs()) memcpy(cur,head,sizeof(cur)),fl+=dfs(S,1e9);
    return;
}
int ans[N];
int main()
{
    init(m),init(c);init(n1);
    Set(head,-1);for(int i=1;i<=n1;++i) init(X1[i]),init(Y1[i]);
    init(n2);int h=n1;
    for(int i=1;i<=n2;++i) idshi[i]=++h;
    for(int i=1;i<=m;++i) idnum[i]=++h;
    for(int i=1;i<=c;++i) idcol[i]=++h;
    T=++h;
    for(int i=1;i<=n1;++i) add_edge(S,i,1),add_edge(i,idnum[X1[i]],1),add_edge(i,idcol[Y1[i]],1);
    for(int i=1;i<=n2;++i) init(X2[i]),init(Y2[i]),add_edge(idshi[i],T,1),add_edge(idnum[X2[i]],idshi[i],1),add_edge(idcol[Y2[i]],idshi[i],1);
    Dinic();bfs();
    for(int v,i=head[S];~i;i=a[i].next) {v=a[i].to;if(v>0&&v<=n1&&!a[i].cap&&!d[v]) ans[v]=1;}
    for(int i=1;i<=n1;++i) puts(ans[i]? "1":"0");
    return 0;
}