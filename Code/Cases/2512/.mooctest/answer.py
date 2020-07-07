#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll read()
{
    ll r=0,f=1;char c=getchar();
    while((c<'0'||c>'9')&&c!='-') c=getchar();
    if(c=='-') f=-1,c=getchar();
    while(c>='0'&&c<='9') r=r*10+c-'0',c=getchar();
    return r*f;
}
struct Segment
{
    ll l,r,sum,add,mul;
    #define l(x) tree[x].l
    #define r(x) tree[x].r
    #define sum(x) tree[x].sum
    #define add(x) tree[x].add
    #define mul(x) tree[x].mul
}tree[100010*4];
ll n,m,h,a[100010];
void build(ll p,ll l,ll r)
{
    l(p)=l,r(p)=r,mul(p)=1,add(p)=0;
    if(l==r){sum(p)=a[l];return ;}
    ll mid=(l+r)>>1;
    build(p*2,l,mid);
    build(p*2+1,mid+1,r);
    sum(p)=sum(p*2)+sum(p*2+1);
    sum(p)%=h;
}
void spread(ll p)
{
    if(add(p)||mul(p)!=1)
    {
        sum(p*2)=(sum(p*2)*mul(p))%h;
        sum(p*2+1)= (sum(p*2+1)*mul(p))%h;
        sum(p*2)=(sum(p*2)+add(p)*(r(p*2)-l(p*2)+1))%h;
        sum(p*2+1)=(sum(p*2+1)+add(p)*(r(p*2+1)-l(p*2+1)+1))%h;
        mul(p*2)=(mul(p*2)*mul(p))%h;
        mul(p*2+1)=(mul(p*2+1)*mul(p))%h;
        add(p*2)=(add(p*2)*mul(p))%h;
        add(p*2+1)=(add(p*2+1)*mul(p))%h;
        add(p*2)=(add(p*2)+add(p))%h;
        add(p*2+1)=(add(p*2+1)+add(p))%h;
        add(p)=0;
        mul(p)=1;
    }
}
void change(ll p,ll l,ll r,ll d,ll k)
{
    if(l<=l(p)&&r>=r(p))
    {
        if(k==2)
        {
            sum(p)+=d*(r(p)-l(p)+1);
            add(p)+=d;
            sum(p)%=h;
            add(p)%=h;
        }
        if(k==1)
        {
            sum(p)*=d;
            add(p)*=d;
            mul(p)*=d;
            sum(p)%=h;
            add(p)%=h;
            mul(p)%=h;
        }
        return ;
    }
    spread(p);
    ll mid=(l(p)+r(p))>>1;
    if(l<=mid) change(p*2,l,r,d,k);
    if(r>mid) change(p*2+1,l,r,d,k);
    sum(p)=sum(p*2)+sum(p*2+1);
    sum(p)%=h;
}
ll ask(ll p,ll l,ll r)
{
    if(l<=l(p)&&r>=r(p)) return sum(p);
    spread(p);
    ll mid=(l(p)+r(p))>>1;
    ll ans=0;
    if(l<=mid) ans+=ask(p*2,l,r);
    if(r>mid) ans+=ask(p*2+1,l,r);
    ans%=h;
    return ans;
}
int main()
{
    n=read(),h=read();
    for(int i=1;i<=n;i++) a[i]=read();
    m=read();
    build(1,1,n);   
    for(int i=1;i<=m;i++)
    {
        ll q=read();
        if(q==1)
        {
            ll x=read(),y=read(),z=read();
            change(1,x,y,z,1);
        }
        else if(q==2){
            ll x=read(),y=read(),z=read();
            change(1,x,y,z,2);
        }
        else if(q==3){
            ll x=read(),y=read();
            printf("%lld\n",ask(1,x,y)%h);
        }
    }
    return 0;
}