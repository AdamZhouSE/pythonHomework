#include <cstdio>
const int N=100010;
int head[N],w[N<<1],cnt=0,to[N<<1],next[N<<1];
int n,m,d[N],used[N];
void add(int u,int v,int w0)
{
    to[++cnt]=v;next[cnt]=head[u];w[cnt]=w0;head[u]=cnt;
}
void dfs(int now)
{
    used[now]=1;
    for(int i=head[now];i;i=next[i])
    {
        int v=to[i];
        if(!used[v])
        {
            d[v]=d[now]^w[i];
            used[v]=1;
            dfs(v);
        }
    }
}
int main()
{
    scanf("%d",&n);
    int u,v;
    for(int i=1;i<n;i++)
    {
        scanf("%d%d%d",&u,&v,w);
        add(u,v,w[0]),add(v,u,w[0]);
    }
    dfs(1);
    scanf("%d",&m);
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d",&u,&v);
        printf("%d\n",d[u]^d[v]);
    }
    return 0;
}

