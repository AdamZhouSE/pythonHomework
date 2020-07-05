#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<algorithm>
#define M 200010
#define int long long
using namespace std;
int read()
{
    char ch=getchar();int x=0;
    while(ch>'9'||ch<'0') ch=getchar();
    while(ch<='9'&&ch>='0') x=x*10+ch-'0',ch=getchar();
    return x;
}
struct point{
    int to,next,dis;
}e[M<<1];
int n,m,num,Q,top;
int q[M],head[M],deep[M],dist[M];
int dis[50][M],fa[M][25];
bool vis[M];
struct node{int id,dis;};
bool operator < (node a1,node a2) {return a1.dis>a2.dis;}
void add(int from,int to,int dis)
{
    e[++num].next=head[from];
    e[num].to=to;
    e[num].dis=dis;
    head[from]=num;
}
void dfs(int x,int f)
{
    vis[x]=true; fa[x][0]=f;
    for(int i=head[x];i;i=e[i].next)
    {
        int to=e[i].to;
        if(to==f) continue;
        if(vis[to]) q[++top]=x,q[++top]=to;
        else
        {
            deep[to]=deep[x]+1;
            dist[to]=dist[x]+e[i].dis;
            dfs(to,x);
        }
    }
}
int lca(int x,int y)
{
    if(deep[x]<deep[y]) swap(x,y);
    for(int i=19;i>=0;i--)
        if(deep[fa[x][i]]>=deep[y])
            x=fa[x][i];
    if(x==y) return x;
    for(int i=19;i>=0;i--)
        if(fa[x][i]!=fa[y][i])
            x=fa[x][i],y=fa[y][i];
    return fa[x][0];
}
void Dijkstra(int id)
{
    memset(dis[id],63,sizeof(dis[id]));
    memset(vis,false,sizeof(vis));
    priority_queue<node>Q;
    dis[id][q[id]]=0;
    Q.push((node){q[id],0});
    while(!Q.empty())
    {
        int x=Q.top().id;Q.pop();
        if(vis[x]) continue;
        vis[x]=true;
        for(int i=head[x];i;i=e[i].next)
        {
            int to=e[i].to;
            if(!vis[to]&&dis[id][x]+e[i].dis<dis[id][to])
            {
                dis[id][to]=dis[id][x]+e[i].dis;
                Q.push((node){to,dis[id][to]});
            }
        }
    }
}
#undef int
int main()
{
    #define int long long
    n=read(); m=read();
    for(int i=1;i<=m;i++)
    {
        int a=read(),b=read(),c=read();
        add(a,b,c); add(b,a,c);
    }
    deep[1]=1;dfs(1,0);
    for(int j=1;j<=19;j++)
        for(int i=1;i<=n;i++)
            fa[i][j]=fa[fa[i][j-1]][j-1];
    sort(q+1,q+1+top); top=unique(q+1,q+1+top)-q-1;
    for(int i=1;i<=top;i++) Dijkstra(i);
    Q=read();
    while(Q--)
    {
        int x=read(),y=read();
        int ans=dist[x]+dist[y]-2*dist[lca(x,y)];
        for(int i=1;i<=top;i++) ans=min(ans,dis[i][x]+dis[i][y]);
        printf("%I64d\n",ans);
    }
    return 0;
}