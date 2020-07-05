#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue> 
#define MAXN 100005
#define LL long long
#define INF 2147483640
#define MOD 100000007
#define free(s) freopen("s.txt","r",stdin);
#define lowbit(x) ((x&(-x))) 
using namespace std;
const int L1=1e7+5,L2=1e7+5;
struct node{
    int l,r,cov,len;
};
node p[4*L2];
int n,l[2*L2],r[2*L2],q[2*L2],tot,cnt,ans;
void build(int num,int l,int r)
{
    p[num].l=l;
    p[num].r=r;
    p[num].len=0;
    if(l==r)
        return ;
    int mid=(l+r)>>1;
    build(num<<1,l,mid);
    build((num<<1)|1,mid+1,r);
}
void update(int num,int l,int r,int v)
{
    if(p[num].l==l&&p[num].r==r)
    {
        p[num].cov+=v;
        if(p[num].cov==1)
            p[num].len=q[p[num].r+1]-q[p[num].l];
        if(!p[num].cov)
            if(l==r)
                p[num].len=0;
        else
            p[num].len=p[num<<1].len+p[(num<<1)|1].len;
        return;
    }
    int mid=(p[num].l+p[num].r)>>1;
    if(r<=mid)
        update(num<<1,l,r,v);
    else
        if(l>mid)
            update((num<<1)|1,l,r,v);  
    else
    {
        update(num<<1,l,mid,v);
        update((num<<1)|1,mid+1,r,v);   
    }
    if(!p[num].cov)
        p[num].len=p[num<<1].len+p[(num<<1)|1].len;
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d%d",&l[i],&r[i]);
        q[++tot]=l[i];
        q[++tot]=r[i];
    }
    sort(q+1,q+tot+1);
    cnt=unique(q+1,q+tot+1)-q-1;
    build(1,1,cnt-1);
    for(int i=1;i<=n;i++)
    {
        l[i]=lower_bound(q+1,q+tot+1,l[i])-q;
        r[i]=lower_bound(q+1,q+cnt+1,r[i])-q-1;
        update(1,l[i],r[i],1);
    }
    for(int i=1;i<=n;i++)
    {
        update(1,l[i],r[i],-1);
        ans=max(ans,p[1].len);
        update(1,l[i],r[i],1);
    }
    printf("%d",ans);
    return 0;
}
