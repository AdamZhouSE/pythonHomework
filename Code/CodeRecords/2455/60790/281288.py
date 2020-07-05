#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<queue>

using namespace std;
struct edge
{
    int next,to;
} e[40000];
int head[40000],tot,rt,maxn;
void add(int x,int y)
{
    e[++tot].next=head[x];
    head[x]=tot;
    e[tot].to=y;
}
int n,dp[20000],ind[20000];
int val[20000],f[20000];
void dfs_f__k(int x,int fa)
{
    f[x]=fa;
    for(int i=head[x]; i; i=e[i].next)
    {
        int v=e[i].to;
        if(v!=fa)
            dfs_f__k(v,x);
    }
}
void dfs(int x)
{
    dp[x]=val[x];
    for(int i=head[x]; i; i=e[i].next)
    {
        int v=e[i].to;
        if(v!=f[x])
        {
            dfs(v);
            dp[x]+=max(0,dp[v]);
        }
    }
    maxn=max(maxn,dp[x]);
}
int main()
{
    scanf("%d",&n);
    for(int i=1; i<=n; i++)scanf("%d",&val[i]);
    for(int i=1; i<=n-1; i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        add(a,b);
        add(b,a);
    }
    rt=1;
    dfs_f__k(rt,0);
    dfs(rt);
    printf("%d",maxn);
}
