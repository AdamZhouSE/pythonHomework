struct Edge
{
    int u,v,w;
} e[M];
const int inf=2e9;
int n,m,root;
int pre[N],ine[N];
int vis[N],id[N];
int zhuliu()
{
    int ans=0;
    while(1)
    {
        for(ri i=1; i<=n; ++i) ine[i]=inf;  // 初始化
        for(ri i=1; i<=m; ++i)
        {
            int u=e[i].u,v=e[i].v;
            if(u!=v&&e[i].w<ine[v])  // 遍历所有边，对每个点找到最小的入边
                ine[v]=e[i].w,pre[v]=u;
        }
        for(ri i=1; i<=n; ++i)  // 判定无解
            if(i!=root&&ine[i]==inf) return -1;
        int cnt=0;
        for(ri i=1; i<=n; ++i) vis[i]=id[i]=0;
        for(ri i=1; i<=n; ++i)
        {
            if(i==root) continue;
            ans+=ine[i];
            int v=i;
            while(vis[v]!=i&&!id[v]&&v!=root)  // 找环
            {
                vis[v]=i;
                v=pre[v];
            }
            if(!id[v]&&v!=root)
            {
                id[v]=++cnt;  // 把环上的店标记为同一点
                for(ri u=pre[v]; u!=v; u=pre[u])
                    id[u]=cnt;
            }
        }
        if(cnt==0) break; // 无环，得到解
        for(ri i=1; i<=n; ++i)
            if(!id[i]) id[i]=++cnt;
        for(ri i=1; i<=m; ++i)
        {
            int u=e[i].u,v=e[i].v;
            e[i].u=id[u],e[i].v=id[v];
            if(id[u]!=id[v]) e[i].w-=ine[v]; // 修改边权
        }
        root=id[root];
        n=cnt;
    }
    return ans;
}