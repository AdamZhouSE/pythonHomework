#include<bits/stdc++.h>
using namespace std;
const int N=150;
const int inf=0x3f3f3f3f;
int n,m;
int mapp[N][N];
int dis[N];
int vis[N];
int sum=0;
int ss=0;
 
void prim()
{
    memset(vis,false,sizeof(vis));
    memset(dis,inf,sizeof(dis));
    for(int i=1;i<=n;i++) dis[i]=mapp[1][i];
    vis[1]=1;
    dis[1]=0;
    for(int i=1;i<=n-1;i++){
        int minn=inf;
        int u;
        for(int j=1;j<=n;j++){
            if(!vis[j]&&dis[j]<minn){
                minn=dis[j];
                u=j;
            }
        }
        vis[u]=1;
        sum+=minn;
        for(int j=1;j<=n;j++){
            if(!vis[j]&&mapp[u][j]<dis[j]){
                dis[j]=mapp[u][j];
            }
        }
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin>>n>>m;
    memset(mapp,inf,sizeof(mapp));
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        mapp[a][b]=mapp[b][a]=c;
        ss+=c;
    }
    prim();
    cout<<ss-sum;
    return 0;
}