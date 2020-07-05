#include<bits/stdc++.h>
#define mid ((l+r)>>1)
using namespace std;
const int N=30000+4;
int a[N];
int b[N];
int n,m;
struct node{
    int sum;
    int ch;
}t[4*N];
int q[N][3];
int pos;
void pushdown(int x,int l,int r){
    if(t[x].ch==-1) return;
    t[x<<1].ch=t[x].ch;
    t[x<<1|1].ch=t[x].ch;
    t[x<<1].sum=t[x].ch*(mid-l+1);
    t[x<<1|1].sum=t[x].ch*(r-mid);
    t[x].ch=-1;
}
void build(int x,int l,int r){
    if(l==r){
        t[x].ch=-1;
        t[x].sum=b[l];
        return;
    }
    t[x].ch=-1;
    build(x<<1,l,mid);
    build(x<<1|1,mid+1,r);
    t[x].sum=t[x<<1].sum+t[x<<1|1].sum;
}
int query(int x,int l,int r,int L,int R){
    if(L<=l&&r<=R){
        return t[x].sum;
    }
    pushdown(x,l,r);
    int ret=0;
    if(L<=mid) ret+=query(x<<1,l,mid,L,R);
    if(mid<R) ret+=query(x<<1|1,mid+1,r,L,R);
    return ret;
}
void chan(int x,int l,int r,int L,int R,int c){
    if(L<=l&&r<=R){
        t[x].ch=c;
        t[x].sum=(r-l+1)*c;
        return;
    }
    pushdown(x,l,r);
    if(L<=mid) chan(x<<1,l,mid,L,R,c);
    if(mid<R) chan(x<<1|1,mid+1,r,L,R,c);
    t[x].sum=t[x<<1].sum+t[x<<1|1].sum;
}
int main(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]);
    for(int i=1;i<=m;i++){
        scanf("%d%d%d",&q[i][0],&q[i][1],&q[i][2]);
    }
    scanf("%d",&pos);
    int l=1,r=n;
    int ans;
    while(l<=r){
        int MID=(l+r)>>1;
        
        for(int i=1;i<=n;i++){
            if(a[i]>=MID) b[i]=1;
            else b[i]=0;
            //cout<<b[i]<<" ";
        }//cout<<endl;
        build(1,1,n);
        
        //cout<<l<<" "<<r<<" mid "<<MID<<endl;
        for(int i=1;i<=m;i++){
            //cout<<i<<" "<<q[i][1]<<" "<<q[i][2]<<endl;
            
            int sum1=query(1,1,n,q[i][1],q[i][2]);
            int sum0=q[i][2]-q[i][1]+1-sum1;
            
            //cout<<" sum "<<sum1<<" "<<sum0<<endl;            
            if(q[i][0]){//down
                chan(1,1,n,q[i][1],q[i][1]+sum1-1,1);
                chan(1,1,n,q[i][1]+sum1,q[i][2],0);
            }
            else{//up
                chan(1,1,n,q[i][1],q[i][1]+sum0-1,0);
                chan(1,1,n,q[i][1]+sum0,q[i][2],1);
            }
        }
        
        int lp=query(1,1,n,pos,pos);
        if(lp==1) ans=MID,l=MID+1;
        else r=MID-1;
    }
    printf("%d",ans);
    return 0;
}