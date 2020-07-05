#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
const int N=300;
int n,m,map[N][N],first[N],next[N*N],go[N*N],tot=0,maxx=0,belong[N],k,used[N];
inline void comb(int a,int b)
{
  next[++tot]=first[a],first[a]=tot,go[tot]=b;
}
inline void clear()
{
  tot=0;
  memset(first,0,sizeof(first));
  memset(belong,0,sizeof(belong));
  memset(used,0,sizeof(used));
}
inline bool find(int u,int T)
{
  for(int e=first[u];e;e=next[e])
  {
    if(used[go[e]]!=T)
    {
      used[go[e]]=T;
      if(!belong[go[e]]||find(belong[go[e]],T))
      {
        belong[go[e]]=u;
        return true;
      }
    } 
  }
  return false;
}
int main()
{
 // freopen("a.in","r",stdin);
  scanf("%d%d%d",&n,&m,&k);
  for(int i=1;i<=n;i++)
    for(int j=1;j<=m;j++)
    {  
      scanf("%d",&map[i][j]);
      maxx=max(maxx,map[i][j]);
    }
  int l=1,r=maxx;
  while(l<=r)
  {
    clear();
    int mid=(l+r)/2;
    for(int i=1;i<=n;i++)
      for(int j=1;j<=m;j++)
        if(map[i][j]<=mid)
          comb(i,j);
    int temp=0;
    for(int i=1;i<=n;i++)      
      if(find(i,i)) temp++;   
    if(temp>=n-k+1)  r=mid-1;
    else l=mid+1;
  }
  cout<<l<<endl;
  return 0;
}