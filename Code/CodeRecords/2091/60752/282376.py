#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
#define N 1500
int ans,mate[N],n,m;
bool vis[N],a[N][N];
bool check(int x)
{
    for(int i=0;i<n;i++)
      if(a[x][i]&&!vis[i]) 
      {
          vis[i]=true;
          if(mate[i]==-1||check(mate[i]))
          {
              mate[i]=x;
              return true;
          }
      }
    return false;
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        a[i][x]=a[i][y]=true;
    }
    memset(mate,-1,sizeof(mate));
    for(int i=1;i<=m;i++)
    {
        memset(vis,0,sizeof(vis));
        if(check(i)) ans++;
        else break;
    }
    printf("%d\n",ans);
    return 0;
}