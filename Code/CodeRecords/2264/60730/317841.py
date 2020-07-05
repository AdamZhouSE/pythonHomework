#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
using namespace std;
int n,m,a[505],t,low[505],dfn[505],cnt,sum,p1,p;
bool iscut[505];
vector<int>G[505];
void Tarjan(int u,int fa)
{
    p1++;
    low[u]=p1;
    dfn[u]=p1;
    int son=0;
    for(int i=0; i<G[u].size(); i++)
    {
        int v=G[u][i];
        if(!dfn[v])
        {
            son++;
            Tarjan(v,u);
            if(low[v]>=dfn[u])
                iscut[u]=1;
            low[u]=min(low[u],low[v]);
        }
        else if(v!=fa)
            low[u]=min(low[u],dfn[v]);
    }
    if(u==1&&son==1)
        iscut[u]=0;
}
void dfs(int u)
{
    a[u]=p;
    cnt++;
    for(int i=0; i<G[u].size(); i++)
    {
        int v=G[u][i];
        if(iscut[v]&&a[v]!=p)
        {
            sum++;
            a[v]=p;
        }
        else if(!a[v])
            dfs(v);
    }
}
int main()
{
    while(scanf("%d",&m)!=-1&&m)
    {
        t++;
        p1=0;
        n=0;
        memset(low,0,sizeof(low));
        memset(dfn,0,sizeof(dfn));
        memset(iscut,0,sizeof(iscut));
        memset(G,0,sizeof(G));
        int a1,b1;
        for(int i=1; i<=m; i++)
        {
            scanf("%d%d",&a1,&b1);
            n=max(n,a1);
            n=max(n,b1);
            G[a1].push_back(b1);
            G[b1].push_back(a1);
        }
        for(int i=1; i<=n; i++)
        {
            if(!dfn[i])
                Tarjan(i,-1);
        }
        p=0;
        memset(a,0,sizeof(a));
        int ans1=0;
        long long ans2=1;
        for(int i=1; i<=n; i++)
        {
            if(!a[i]&&!iscut[i])
            {
                cnt=0;
                sum=0;
                p++;
                dfs(i);
                if(sum==0)
                {
                    ans1+=2;
                    ans2*=(cnt-1)*cnt/2;
                }
                if(sum==1)
                {
                    ans1++;
                    ans2*=cnt;
                }
            }
        }
        printf("Case %d: %d %lld\n",t,ans1,ans2);
    }
}