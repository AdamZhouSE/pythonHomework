#include<cmath>
#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
const int maxn = 1000100;
struct node{
    int l,r,id,block;
    bool operator < (const node&a)const
    {
        if(block==a.block)return r<a.r;
        return block < a.block; 
    }
}q[maxn]; 
int a[maxn],cnt[maxn],ans[maxn];
int n,m,k,pos,tmp;
void del(int x)
{
    cnt[a[x]]--;
    if (cnt[a[x]]==1)tmp--;
}
void add(int x)
{
    cnt[a[x]]++;
    if (cnt[a[x]]==2)tmp++;
}
void work()
{
    int l=1,r=0;
    for(int i =1;i<=m;++i)
    {
        while(l>q[i].l)l--,add(l);
        while(r<q[i].r)r++,add(r);
        while(l<q[i].l)del(l),l++;
        while(r>q[i].r)del(r),r--;
        ans[q[i].id] = tmp;
    }
}
int main()
{
     scanf("%d%d%d",&n,&k,&m);
     pos = sqrt(n);
     for(int i=1;i<=n;++i)
         scanf("%d",a+i);
    for (int i=1;i<=m;++i)
    {
        scanf("%d%d",&q[i].l,&q[i].r);
        q[i].block = (q[i].l-1)/pos+1;
        q[i].id=i;
    }
    sort(q+1,q+m+1);
    work();
    for(int i=1;i<=m;++i)
        printf("%d\n",ans[i]);
    return 0;
}