#include<bits/stdc++.h>
using namespace std;
int mm[1010];
int vis[1010];
int line[105][105];
int n,m,k;
int found(int x)
{
    for(int i=1;i<=n;i++)
    {
        if(vis[i]==0&&line[x][i]==1)
        { 
             vis[i]=1;
             if(mm[i]==0||found(mm[i]))//找mm[i]有没有另一条路
             {
                 mm[i]=x;
                 return 1;
             }
        }
    }
    return 0;
}
int countt()
{
    int sum=0;
    memset(mm,0,sizeof(mm));
    for(int i=1;i<=n;i++)
    {
        memset(vis,0,sizeof(vis));
        if(found(i))
            sum++;
    }
    return sum;
}
int main()
{
      int r=1;
      while(~scanf("%d%d%d",&n,&m,&k))
      {
          memset(vis,0,sizeof(vis));
          memset(mm,0,sizeof(mm));
          memset(line,0,sizeof(line));
          for(int i=0;i<k;i++)
          {
              int a,b;
              scanf("%d%d",&a,&b);
              line[a][b]=1;
          }
          int temp=countt();
          int cnt=0;
          for(int i=1;i<=n;i++)
          {
              for(int j=1;j<=m;j++)
              {
                  if(line[i][j]==1)
                  {
                      line[i][j]=0;
                      if(countt()<temp)
                      cnt++;
                      line[i][j]=1;
                  }
              }
          }
          printf("Board %d have %d important blanks for %d chessmen.\n",r++,cnt,temp);
      }
}