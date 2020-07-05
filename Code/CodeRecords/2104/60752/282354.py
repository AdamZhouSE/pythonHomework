#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
#define N 200010

int fa[N],d[N];

int mmin(int x,int y) {return x<y?x:y;}
int mabs(int x) {return x<0?-x:x;}
int ffind(int x)
{
    if (fa[x]!=x)
    {
      int y=fa[x];
      fa[x]=ffind(y);
      d[x]+=d[y];
    }
    return fa[x];
}
int main()
{
    int n,x,y;
    scanf("%d",&n);
    int mn=n;
    for (int i=1;i<=n;i++) fa[i]=i,d[i]=0;
    for (int i=1;i<=n;i++)
    {
      scanf("%d",&y);
      x=i;
      int fx=ffind(x),fy=ffind(y);
      if (fx!=fy)
      {
        fa[x]=fy;
        d[x]=d[y]+1;
      }
      else mn=mmin(mn,d[y]+1);
    }
    cout<<mn;
    return 0;
}
