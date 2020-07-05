#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
struct Node
{
    int s,t,m;
}a[50001];
int lazy[80001],c1[80001],k,n,c,ans;
bool cmp(Node a,Node b)
{
    return (a.t<b.t||(a.t==b.t&&a.s>b.s));
}
void pushdown(int rt)
{
    if (lazy[rt])
    {
        c1[rt*2]+=lazy[rt];
        lazy[rt*2]+=lazy[rt];
        c1[rt*2+1]+=lazy[rt];
        lazy[rt*2+1]+=lazy[rt];
        lazy[rt]=0;
    }
}
int query(int rt,int l,int r,int L,int R)
{
    if (l>=L&&r<=R)
    {
        return c1[rt];
    }
    pushdown(rt);
     int mid=(l+r)/2;
     int s=0;
     if (L<=mid) s=max(s,query(rt*2,l,mid,L,R));
     if (R>mid) s=max(s,query(rt*2+1,mid+1,r,L,R));
     return s;
}
void add(int rt,int l,int r,int L,int R,int d)
{
    if (l>=L&&r<=R)
    {
        c1[rt]+=d;
        lazy[rt]+=d;
        return;
    }
    pushdown(rt);
    int mid=(l+r)/2;
    if (L<=mid) add(rt*2,l,mid,L,R,d);
     if (R>mid) add(rt*2+1,mid+1,r,L,R,d);
     c1[rt]=max(c1[rt*2],c1[rt*2+1]);
}
int main()
{int i,j;
    cin>>k>>n>>c;
     for (i=1;i<=k;i++)
     {
         scanf("%d%d%d",&a[i].s,&a[i].t,&a[i].m);
         a[i].t--;
     }
     sort(a+1,a+k+1,cmp);
     for (i=1;i<=k;i++)
     {
         int x=min(a[i].m,c-query(1,1,n,a[i].s,a[i].t));
          add(1,1,n,a[i].s,a[i].t,x);
          ans+=x;
     }
     cout<<ans;
}