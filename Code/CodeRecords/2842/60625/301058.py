#include <cstdio>
int father[2001];
int vis[2001];
int ans;
void dfs(int x,int h)
{
    vis[x]=1;
    if(father[x]==-1)
    {
        if(h>ans)
            ans=h;
        return;
    }
    return dfs(father[x],h+1);
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",&father[i]);
    for(int i=1;i<=n;i++)
        if(!vis[i])
            dfs(i,1);
    printf("%d\n",ans);
    return 0;
}


