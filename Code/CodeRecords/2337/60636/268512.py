#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int n,m,cnt1,cnt2;
char map[60][60];
int G[2505][2505],row[60][60],col[60][60];
int vis[2505],match[2505];
bool dfs(int u)
{
    for(int v=1;v<=cnt2;v++)
    {
        if(G[u][v]&&!vis[v])
        {
            vis[v]=1;
            if(!match[v]||dfs(match[v]))
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
    cin>>n>>m;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            cin>>map[i][j];
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
        {
            if(j==1||map[i][j-1]=='#')
                cnt1++;
            row[i][j]=cnt1;
        }
    for(int i=1;i<=m;i++)
        for(int j=1;j<=n;j++)
        {
            if(j==1||map[j-1][i]=='#')
                cnt2++;
            col[j][i]=cnt2;
        }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            if(map[i][j]=='*')
                G[row[i][j]][col[i][j]]=1;
    int ans=0;
    for(int i=1;i<=cnt1;i++)
    {
        memset(vis,0,sizeof(vis));
        if(dfs(i))
            ans++;
    }
    cout<<ans;
    return 0;
}