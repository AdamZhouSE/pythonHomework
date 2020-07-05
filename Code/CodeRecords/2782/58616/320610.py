
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define N 50000
using namespace std;
int n,m,sum,root,sz;
int key[N],size[N],cnt[N],ch[N][3],fa[N];
const int inf=1e9;
void clear(int x)
{
  fa[x]=key[x]=size[x]=cnt[x]=ch[x][1]=ch[x][0]=0;
}
void update(int x)
{
 size[x]=size[ch[x][0]]+size[ch[x][1]]+cnt[x];
}
int get(int x)
{
  return ch[fa[x]][1]==x;
}
void rotate(int x)
{
  int y=fa[x]; int z=fa[y]; int which=get(x);
  if (z) ch[z][ch[z][1]==y]=x;
  ch[y][which]=ch[x][which^1]; fa[ch[x][which^1]]=y;
  ch[x][which^1]=y; fa[y]=x; fa[x]=z;
  update(y); update(x);
}
void splay(int x)
{
 for (int f;(f=fa[x]);rotate(x))
 if (fa[f]) rotate(get(x)==get(f)?f:x); 
 root=x;
}
void insert(int x)
{
  if (!root)
  {
  	sz++; root=sz; clear(sz); size[sz]=cnt[sz]=1; key[sz]=x; return;
  }
  int now=root;
  while(true)
  {
   if (x==key[now])
    {
      cnt[now]++; update(now); splay(now); return;
    }
   int f=now;
   now=ch[now][x>key[now]];
   if (!now)
   {
    sz++; ch[f][x>key[f]]=sz; clear(sz); size[sz]=cnt[sz]=1;
    key[sz]=x; fa[sz]=f; update(f); splay(sz); return;
   }
  }
}
int pre()
{
 int now=ch[root][0];
 while (ch[now][1]) now=ch[now][1];
 return now;
}
int next()
{
 int now=ch[root][1];
 while(ch[now][0]) now=ch[now][0];
 return now;
}
int main()
{
  scanf("%d",&n);
  for (int i=1;i<=n;i++)
  {
   int x; scanf("%d",&x);
   insert(x);
   if(i!=1)
    {
      if (cnt[root]>1) continue;
      if (pre()&&next())
       sum+=min(abs(key[pre()]-x),abs(key[next()]-x));
      else 
	  if (pre()) sum+=abs(key[pre()]-x);
      else
      if (next()) sum+=abs(key[next()]-x);
    }
   else
    sum=x;
  }
  printf("%d",sum);
}