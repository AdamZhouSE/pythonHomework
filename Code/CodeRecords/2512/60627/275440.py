#include<iostream>
#include<cstring>
#include<cstdio>
#define maxn 100001
using namespace std;
int n,m,mod,val[maxn];
inline int read(){
    register int x(0),f(1); register char c(getchar());
    while(c<'0'||'9'<c){ if(c=='-') f=-1; c=getchar(); }
    while('0'<=c&&c<='9') x=(x<<1)+(x<<3)+(c^48),c=getchar();
    return x*f;
}

struct SegmentTree{
    int l,r;
    long long val,add,mul;
}t[maxn<<2];
inline void down(const int &d){
    t[d<<1].val=(t[d<<1].val*t[d].mul % mod+(t[d<<1].r-t[d<<1].l+1)*t[d].add % mod) % mod;
    t[d<<1|1].val=(t[d<<1|1].val*t[d].mul % mod+(t[d<<1|1].r-t[d<<1|1].l+1)*t[d].add % mod) % mod;
    t[d<<1].mul=(t[d<<1].mul*t[d].mul) % mod;
    t[d<<1|1].mul=(t[d<<1|1].mul*t[d].mul) % mod;
    t[d<<1].add=(t[d<<1].add*t[d].mul % mod+t[d].add) % mod;
    t[d<<1|1].add=(t[d<<1|1].add*t[d].mul % mod+t[d].add) % mod;
    t[d].add=0ll,t[d].mul=1ll;
}
void build(int d,int l,int r){
    t[d].l=l,t[d].r=r,t[d].add=0ll,t[d].mul=1ll;
    if(l==r){ t[d].val=val[l] % mod; return; }
    int mid=l+r>>1;
    build(d<<1,l,mid),build(d<<1|1,mid+1,r);
    t[d].val=(t[d<<1].val+t[d<<1|1].val) % mod;
}
void change_mul(int d,const int &l,const int &r,const int &val){
    if(l<=t[d].l&&t[d].r<=r){
        t[d].val=(t[d].val*val) % mod,t[d].mul=(t[d].mul*val) % mod,t[d].add=(t[d].add*val) % mod;
        return;
    }
    down(d);
    int mid=t[d].l+t[d].r>>1;
    if(l<=mid) change_mul(d<<1,l,r,val);
    if(r>mid) change_mul(d<<1|1,l,r,val);
    t[d].val=(t[d<<1].val+t[d<<1|1].val) % mod;
}
void change_add(int d,const int &l,const int &r,const int &val){
    if(l<=t[d].l&&t[d].r<=r){
        t[d].val=(t[d].val+(t[d].r-t[d].l+1)*val % mod) % mod,t[d].add=(t[d].add+val) % mod;
        return;
    }
    down(d);
    int mid=t[d].l+t[d].r>>1;
    if(l<=mid) change_add(d<<1,l,r,val);
    if(r>mid) change_add(d<<1|1,l,r,val);
    t[d].val=(t[d<<1].val+t[d<<1|1].val) % mod;
}
long long getsum(int d,const int &l,const int &r){
    if(l<=t[d].l&&t[d].r<=r) return t[d].val;
    down(d);
    int mid=t[d].l+t[d].r>>1;
    long long ans=0ll;
    if(l<=mid) ans=(ans+getsum(d<<1,l,r)) % mod;
    if(r>mid) ans=(ans+getsum(d<<1|1,l,r)) % mod;
    return ans;
}

int main(){
    n=read(),mod=read();
    for(register int i=1;i<=n;i++) val[i]=read();
    m=read();
    build(1,1,n);
    for(register int i=1;i<=m;i++){
        int op=read(),l=read(),r=read();
        if(op==1) change_mul(1,l,r,read());
        if(op==2) change_add(1,l,r,read());
        if(op==3) printf("%lld\n",getsum(1,l,r));
    }
    return 0;
}