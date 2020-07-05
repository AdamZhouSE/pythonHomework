#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const int MAXN=200010;

int n,m;
struct index{
    int x,y;
    friend bool operator<(const index a,const index b){
        return a.y<b.y;
    }
}a[MAXN];
int b[MAXN];
int mp[MAXN];
int sx,sy,sd;

inline int read(){
    int x=0; char c;
    do c=getchar(); while(c<'0'||c>'9');
    while(c>='0'&&c<='9')
        x=x*10+c-48,c=getchar();
    return x;
}
struct PreSegTree{
    struct index{
        int l,r,ls,rs,d;
        index(){
            l=r=ls=rs=d=0;
        }
    }e[MAXN*4];
    int len;
    int root[MAXN];
    PreSegTree(){
        len=0;root[0]=1;
    }
    void buildtree(int l,int r){
        int me=++len;
        e[me].l=l;e[me].r=r;
        if(l==r) return;
        int mid=(l+r)/2;
        e[me].ls=len+1;buildtree(l,mid);
        e[me].rs=len+1;buildtree(mid+1,r);
    }
    void grow(int rt,int x){
        int l=e[rt].l,r=e[rt].r,me=++len;
        e[me].l=l;e[me].r=r;
        if(l==r){
            e[me].d=e[rt].d+1;
            return;
        }
        int mid=(l+r)/2;
        if(x<=mid){
            e[me].ls=len+1;e[me].rs=e[rt].rs;
            grow(e[rt].ls,x);
        }else{
            e[me].ls=e[rt].ls;e[me].rs=len+1;
            grow(e[rt].rs,x);
        }
        e[me].d=e[e[me].ls].d+e[e[me].rs].d;
    }
    void insert(int x,int d){
        root[x]=len+1;
        grow(root[x-1],d);
    }
    int query(int rootl,int rootr,int k){
        int LS=e[rootl].ls,RS=e[rootr].ls;
        int D=e[RS].d-e[LS].d;
        if(e[rootl].l==e[rootl].r) return e[rootl].r;
        if(k<=D) return query(LS,RS,k);
        else return query(e[rootl].rs,e[rootr].rs,k-D);
    }
}T;
int main(){
    n=read();m=read();
    T.buildtree(1,n);
    for(int i=1;i<=n;++i)
        a[i].x=i,a[i].y=read();
    sort(a+1,a+n+1);
    int tmp=0,last=-0x3f3f3f3f;
    for(int i=1;i<=n;++i){
        if(a[i].y!=last){
            ++tmp;
            mp[tmp]=a[i].y;
        }
        b[a[i].x]=tmp;
        last=a[i].y;
    }
    for(int i=1;i<=n;++i)
        T.insert(i,b[i]);
    for(int i=1;i<=m;++i){
        sx=read();sy=read();sd=read();
        printf("%d\n",mp[T.query(T.root[sx-1],T.root[sy],sd)]);
    }
}