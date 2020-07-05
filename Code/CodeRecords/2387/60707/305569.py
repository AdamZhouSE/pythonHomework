#include<cstdio>
#include<cstring>
#define lch k<<1
#define rch k<<1|1
using namespace std;
const int N=1e5+5,M=N<<2;
int n,m,p,a[N],q[N][3];
int sum[M],tag[M];
inline void opera(int k,int sz,int v){
    sum[k]=sz*v;
}
inline void pushdown(int k,int l,int r){
    if(~tag[k]){
        int mid=(l+r)>>1;
        tag[lch]=tag[k];opera(lch,mid-l+1,tag[k]);
        tag[rch]=tag[k];opera(rch,r-mid,tag[k]);
        tag[k]=-1;
    }
}
void change(int k,int l,int r,int x,int y,int v){
    if(x>y) return ;
    if(l==x&&r==y){
        opera(k,r-l+1,v);
        tag[k]=v;
        return ;
    }
    pushdown(k,l,r);
    int mid=(l+r)>>1;
    if(y<=mid) change(lch,l,mid,x,y,v);
    else if(x>mid) change(rch,mid+1,r,x,y,v);
    else change(lch,l,mid,x,mid,v),change(rch,mid+1,r,mid+1,y,v);
    sum[k]=sum[lch]+sum[rch];
}
int query(int k,int l,int r,int x,int y){
    if(l==x&&r==y) return sum[k];
    pushdown(k,l,r);
    int mid=(l+r)>>1;
    if(y<=mid) return query(lch,l,mid,x,y);
    else if(x>mid) return query(rch,mid+1,r,x,y);
    else return query(lch,l,mid,x,mid)+query(rch,mid+1,r,mid+1,y);
}
inline int work(int now){
    memset(sum,0,sizeof sum);
    memset(tag,-1,sizeof tag);
    for(int i=1;i<=n;i++) change(1,1,n,i,i,a[i]>=now);
    for(int i=1,t;i<=m;i++){
        t=query(1,1,n,q[i][1],q[i][2]);
        if(!q[i][0]){
            change(1,1,n,q[i][1],q[i][2]-t,0);
            change(1,1,n,q[i][2]-t+1,q[i][2],1);
        }
        else{
            change(1,1,n,q[i][1],q[i][1]+t-1,1);
            change(1,1,n,q[i][1]+t,q[i][2],0);
        }
    }
    return query(1,1,n,p,p);    
}
int main(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]);
    for(int i=1;i<=m;i++) scanf("%d%d%d",&q[i][0],&q[i][1],&q[i][2]);
    scanf("%d",&p);
    int l=1,r=n,mid,ans;
    while(l<=r){
        mid=(l+r)>>1;
        if(work(mid)) l=mid+1,ans=mid;
        else r=mid-1;
    }
    printf("%d\n",ans);
    return 0;
}

