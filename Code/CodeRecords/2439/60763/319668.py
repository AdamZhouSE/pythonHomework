#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include<cstring> 
using namespace std;
const int N=100005;
int n,m,k=0,head[N],dis[N];
bool visit[N];
struct node
{int to,next,w;}edge[N*2];
void add(int u,int v,int w)
{
    edge[++k].to=v;edge[k].next=head[u];edge[k].w=w;head[u]=k;
}
void dfs(int id,int val)
{
    dis[id]=val;visit[id]=true;
    for(int i=head[id];i;i=edge[i].next)
        if(!visit[edge[i].to])
            dfs(edge[i].to,val^edge[i].w);//处理异或值 
}
int main()
{
    scanf("%d",&n);
    int u,v,w;
    for(int i=1;i<n;i++)
    {
        scanf("%d%d%d",&u,&v,&w);
        add(u,v,w);add(v,u,w);//建边 
    }
    dfs(1,0);scanf("%d",&m);
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d",&u,&v);
        printf("%d\n",dis[u]^dis[v]);
    }
}