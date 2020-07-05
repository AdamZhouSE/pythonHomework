#include<bits/stdc++.h>
#pragma GCC optimize(2)
#define MAXN 200010
#define maxnode 50010
#define sigma_size 26
#define md 1000000007
#define INF 0x3f3f3f3f

using namespace std;
typedef long long LL;

struct node 
{                         
    int l,r;
    int min_n;
}tr[MAXN<<2];
int n,q;

inline int _min(int a,int b){return a<b?a:b;}

inline int read(){
    char c;int f=0,x=0;while(!isdigit(c=getchar()))if(c==45)f=1;
    while(isdigit(c))x=(x<<1)+(x<<3)+(c^48),c=getchar();return f?-x:x;
}

void build(int id,int l,int r)
{
    tr[id].l=l,tr[id].r=r,tr[id].min_n=INF;
    if(l==r)
    {
        tr[id].min_n=INF;
        return ;
    }
    int mid=(l+r)>>1;
    build(id<<1,l,mid);
    build(id<<1|1,mid+1,r);
    tr[id].min_n=_min(tr[id<<1].min_n,tr[id<<1|1].min_n);
}

int query(int id,int l,int r)
{
    if(tr[id].l>=l&&tr[id].r<=r)
    {
        return tr[id].min_n;
    }
    int mid=(tr[id].l+tr[id].r)>>1;
    int ans=INF;
    if(l<=mid)
        ans=_min(ans,query(id<<1,l,r));
    if(r>mid)
        ans=_min(ans,query(id<<1|1,l,r));
    return ans;
}

void update(int id,int pp,int val)
{
    if(tr[id].l==tr[id].r)
    {
        tr[id].min_n=_min(tr[id].min_n,val);
        return ;
    }
    int mid=(tr[id].l+tr[id].r)>>1;
    if(pp<=mid)
        update(id<<1,pp,val);
    else
        update(id<<1|1,pp,val);
    tr[id].min_n=_min(tr[id<<1].min_n,tr[id<<1|1].min_n);
}



int main()
{
    scanf("%d %d",&n,&q);
    build(1,1,n); 
    char op[100];
    int u,v;
    for(int i=1;i<=q;i++)
    {
        scanf("%s",op);
        u=read(),v=read();
        if(op[0]=='M')
        {
            update(1,v,u); 
        }
        else if(op[0]=='D')
        {
            if(query(1,v,n)>u)
            {
                printf("-1\n");
            }
            else
            {
                int L=v,R=n;
                while(L<R)
                {
                    int mid=(L+R)>>1;
                    if(query(1,L,mid)<=u)
                        R=mid;
                    else
                        L=mid+1;
                }
                printf("%d\n",R);
            }
        }
    }
    return 0;
}