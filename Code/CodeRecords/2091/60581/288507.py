#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
const int maxn=1000+5;
int n,m,ans,edge,to[maxn*2],head[maxn],next[maxn*2],match[maxn];
bool vis[maxn];
void edge_add(int u,int v)
{
    to[++edge]=v;
    next[edge]=head[u];
    head[u]=edge;
}
bool DFS(int u)
{
    for (int E=head[u];E;E=next[E])
    {
        int v=to[E];
        if (!vis[v])
        {
            vis[v]=true;
            if (!match[v]||DFS(match[v]))
            {
                match[v]=u;
                return true;
            }
        }
    }
    return false;
}
int main()
{
//  freopen("hungary.in","r",stdin);
    scanf("%d%d",&n,&m);
    for (int i=1;i<=m;i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        x++; y++;
        edge_add(i,x);
        if (x==y) continue;
        edge_add(i,y);
    }
    for (int i=1;i<=n;i++)
    {
        memset(vis,false,sizeof(vis));
        if (DFS(i)) ans++;
        else break;
    }
    cout << ans << endl;
    return 0;
}