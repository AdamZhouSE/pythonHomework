#include<cstdio>
#include<algorithm>
using namespace std;

template<typename T>inline void read(T &x){
    T f=1;char ch=getchar();
    for(;ch<'0'||ch>'9';ch=getchar())if(ch=='-')f=-1;
    for(x=0;ch>='0'&&ch<='9';ch=getchar())x=x*10+ch-'0';
    x*=f;
}

typedef long long LL;
const int maxn=100010;
int n,m,num,head[maxn],dfn[maxn],cnt,tL[maxn],tR[maxn],dep[maxn];
LL a[maxn],w[maxn];
struct edge{
    int to,next;
}e[maxn<<1];
struct Segment_Tree{
    #define lc x<<1
    #define rc x<<1|1
    int L[maxn<<2],R[maxn<<2];
    LL add[maxn<<2],tag[maxn<<2];
    void Build(int x,int l,int r){
        L[x]=l;R[x]=r;
        if(l==r)return add[x]=tag[x]=0,void();
        int mid=(l+r)>>1;
        Build(lc,l,mid);
        Build(rc,mid+1,r);
    }
    void pushdown(int x){
        if(add[x]){
            add[lc]+=add[x];
            add[rc]+=add[x];
            add[x]=0;
        }
        if(tag[x]){
            tag[lc]+=tag[x];
            tag[rc]+=tag[x];
            tag[x]=0;
        }
    }
    void Add1(int x,int l,int r,LL val){
        if(R[x]<l||L[x]>r)return;
        if(L[x]>=l&&R[x]<=r)return add[x]+=val,void();
        pushdown(x);
        Add1(lc,l,r,val);
        Add1(rc,l,r,val);
    }
    void Add2(int x,int l,int r,LL val){
        if(R[x]<l||L[x]>r)return;
        if(L[x]>=l&&R[x]<=r)return tag[x]+=val,void();
        pushdown(x);
        Add2(lc,l,r,val);
        Add2(rc,l,r,val);
    }
    LL Query(int x,int pos){
        if(L[x]==R[x])return add[x]+tag[x]*dep[dfn[pos]];
        pushdown(x);
        int mid=(L[x]+R[x])>>1;
        if(pos<=mid)return Query(lc,pos);
        else return Query(rc,pos);
    }
}tree;

void add(int u,int v){
    e[++num].to=v;e[num].next=head[u];head[u]=num;
    e[++num].to=u;e[num].next=head[v];head[v]=num;
}
void Dfs(int x,int fa){
    dep[dfn[tL[x]=++cnt]=x]=dep[fa]+1;
    w[x]=w[fa]+a[x];
    for(int i=head[x];i;i=e[i].next)
        if(e[i].to!=fa)Dfs(e[i].to,x);
    tR[x]=cnt;
}

int main(){
    read(n);read(m);
    for(int i=1;i<=n;i++)read(a[i]);
    for(int i=1,u,v;i<n;i++)
        read(u),read(v),add(u,v);
    Dfs(1,0);tree.Build(1,1,n);
    for(int i=1;i<=n;i++)tree.Add1(1,tL[i],tL[i],w[i]);
    while(m--){
        int opt,x;LL val;
        read(opt);read(x);
        if(opt==1){
            read(val);
            tree.Add1(1,tL[x],tR[x],val);
        }
        else if(opt==2){
            read(val);
            tree.Add2(1,tL[x],tR[x],val);
            tree.Add1(1,tL[x],tR[x],-val*(dep[x]-1));
        }
        else printf("%lld\n",tree.Query(1,tL[x]));
    }
    return 0;
}
