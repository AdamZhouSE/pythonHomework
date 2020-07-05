#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
int a[N];
int c[N];
int n,m;
int ans[N];
struct hs
{
  int head[N];
  int next[N];
  void init()
  {
    memset(head,-1,sizeof(head));
  }
  void insert(int i,int x)
  {
    next[i]=-1;
    if(head[x]==-1) head[x]=i;
    else
    {
      int j=head[x];
      while(next[j]!=-1) j=next[j];
      next[j]=i;
    }
  }
  int find(int i)
  {
    return next[i];
  }
}hp;
struct node
{
  int l,r,index;
  bool operator <(const node &W)const
  {
    return l<W.l;
  }
}nodes[N];
int lowbit(int x)
{
  return x&(-x);
}
void add(int i,int x)
{
  while(i<N)
  {
    c[i]+=x;
    i+=lowbit(i);
  }
}
int  sum(int i)
{
    int res=0;
    while(i>0)
    {
      res+=c[i];
      i-=lowbit(i);
    }
    return res;
}
int main()
{
  hp.init();
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
  {
    scanf("%d",&a[i]);
    if(hp.head[a[i]]==-1) add(i,1);
    hp.insert(i,a[i]);
  }
  scanf("%d",&m);
  for(int i=1;i<=m;i++)
  {
    scanf("%d %d",&nodes[i].l,&nodes[i].r);
    nodes[i].index=i;
  }
  sort(nodes+1,nodes+1+m);
  int j=1;
  for(int i=1;i<=n;i++)
  {
    while(nodes[j].l==i)
    {
      ans[nodes[j].index]=sum(nodes[j].r);
      j++;
    }
    if(j>m) break;
    add(i,-1);
    int pos=hp.find(i);
    if(pos!=-1) add(pos,1);
  }
  for(int i=1;i<=m;i++) cout<<ans[i]<<endl;
}
