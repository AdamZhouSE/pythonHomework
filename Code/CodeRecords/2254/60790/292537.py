#include<iostream>
#include<cstring>
#include<cstdio>
#define N (5000+100)
using namespace std;

struct Edge{int to,next;} edge[N<<3];
int n,m,u,v,head[N],num_edge;
int Dfn[N],Low[N],dfs_num;
int bridge_num,ans;
bool Bridge[N],vis[N],dis[N][N];

void add(int u,int v)
{
    edge[++num_edge].to=v;
    edge[num_edge].next=head[u];
    head[u]=num_edge;
}

void Tarjan(int x,int fa)
{
    Dfn[x]=Low[x]=++dfs_num;
    for (int i=head[x]; i; i=edge[i].next)
        if (!Dfn[edge[i].to])
        {
            Tarjan(edge[i].to,x);
            Low[x]=min(Low[x],Low[edge[i].to]);
            if (Low[edge[i].to]>Dfn[x])
                Bridge[i]=Bridge[(i-1^1)+1]=true;
        }
        else if (Dfn[edge[i].to]<Dfn[x] && edge[i].to!=fa)
            Low[x]=min(Low[x],Dfn[edge[i].to]);
}

void Dfs(int x)
{
    vis[x]=true;
    for (int i=head[x]; i; i=edge[i].next)
    {
        if(Bridge[i]){bridge_num++; continue;}
        if (!vis[edge[i].to]) Dfs(edge[i].to);
    }
}

int main()
{
    scanf("%d%d",&n,&m);
    for (int i=1; i<=m; ++i)
        scanf("%d%d",&u,&v),dis[u][v]=dis[v][u]=true;
    for (int i=1; i<=n; ++i)
        for (int j=i+1; j<=n; ++j)
            if (dis[i][j])
                add(i,j),add(j,i);
    for (int i=1; i<=n; ++i)
        if (!Dfn[i])
            Tarjan(i,0);
    for (int i=1; i<=n; ++i)
        if (!vis[i])
        {
            bridge_num=0;
            Dfs(i);
            if (bridge_num==1)
                ans++;
        }
    printf("%d\n",(ans+1)/2);
}