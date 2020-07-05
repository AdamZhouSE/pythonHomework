#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define pd(ch) ch!='R'&&ch!='Q'&&ch!='D'
using namespace std;
const int maxn=5e4+5,maxt=5e2+5;
int n,m,q,tot,id[maxn],L[maxt],R[maxt],ansL[maxt],ansR[maxt],st[maxn];
int vis[maxn];
//id每个点所在组号，L每组左边界，R每组右边界
//vis每个点的状态，ansL和ansR表示每组最左边第一个和最右边第一个拆了的点
void ins(int x)
{
    if (vis[x]) return;
    vis[x]=1;st[++st[0]]=x;
    int y=id[x];
    if (ansL[y]==-1||ansL[y]>x) ansL[y]=x;
    if (ansR[y]<x) ansR[y]=x;
}
void del(int x)
{
    if (!vis[x]) return;
    vis[x]=0;int y=id[x],i;
    if (ansL[y]==x)
      for (i=L[y],ansL[y]=-1;i<=R[y];i++)
        if (vis[i]) {ansL[y]=i;break;}
    if (ansR[y]==x)
      for (i=R[y],ansR[y]=-1;i>=L[y];i--)
        if (vis[i]) {ansR[y]=i;break;}
}
int fin(int x)
{
    pair<int,int>ans;
    ans.first=0,ans.second=n+1;
    int y=id[x];
    if (ansL[y]!=-1&&ansL[y]<=x)
    {
        for (int i=x;i>=L[y];i--)
          if (vis[i]) {ans.first=i;break;}
    }else
    {
        for (int i=y-1;i>=1;i--)
          if (ansR[i]!=-1) {ans.first=ansR[i];break;}
    }
    if (ansR[y]!=-1&&ansR[y]>=x)
    {
        for (int i=x;i<=R[y];i++)
          if (vis[i]) {ans.second=i;break;}
    }else
    {
        for (int i=y+1;i<=tot;i++)
          if (ansL[i]!=-1) {ans.second=ansL[i];break;}
    }
    return max(0,ans.second-ans.first-1);
}
int main()
{
    scanf("%d%d",&n,&q);
    m=sqrt(n);
    for (int i=1;i<=n;)
    {
        tot++;ansL[tot]=-1;ansR[tot]=-1;
        L[tot]=i;R[tot]=min(i+m-1,n);
        for (;i<=R[tot];i++) id[i]=tot;
    }
    for (int i=1,x;i<=q;i++)
    {
        char ch=getchar();
        while (pd(ch)) ch=getchar();
        if (ch!='R') scanf("%d",&x);
        if (ch=='R') {if (st[0]>0) del(st[st[0]--]);}else
        if (ch=='Q') printf("%d\n",fin(x));else
        if (ch=='D') ins(x);
    }
    return 0;
}
