#include<bits/stdc++.h>
using namespace std;
#define MAXN 1000000+10
typedef long long LL;
int n,tot=0,ans=0,pos[4][MAXN],dp[5][MAXN],tr[5][MAXN*52];
LL a[5][MAXN],b[MAXN*4];
void pushup(int t,int k){tr[t][k]=max(tr[t][k<<1],tr[t][k<<1|1]);}
void build(int t,int k,int l,int r){
    tr[t][k]=0;
    if(l==r)return;
    int mid=(l+r)>>1;
    build(t,k<<1,l,mid);
    build(t,k<<1|1,mid+1,r);
}
void update(int t,int k,int l,int r,int p,int val){
    if(l==r&&l==p){
        tr[t][k]=val;
        return;
    }
    int mid=(l+r)>>1;
    if(p<=mid)update(t,k<<1,l,mid,p,val);
    else update(t,k<<1|1,mid+1,r,p,val);
    pushup(t,k);
}
int query(int t,int k,int l,int r,int L,int R){
    if(l>=L&&r<=R)return tr[t][k];
    int mid=(l+r)>>1;
    if(R<=mid)return query(t,k<<1,l,mid,L,R);
    else if(L>mid)return query(t,k<<1|1,mid+1,r,L,R);
    else return max(query(t,k<<1,l,mid,L,R),query(t,k<<1|1,mid+1,r,L,R));
}
int main(){
    //freopen("data.in","r",stdin);
    scanf("%d",&n);
    for(int i=1;i<=3;i++)
        for(int j=1;j<=n;j++){
            scanf("%lld",&a[i][j]);
            b[++tot]=a[i][j];        
        }
    sort(b+1,b+tot+1);
    tot=unique(b+1,b+tot+1)-b,tot--;
    for(int i=1;i<=4;i++)build(i,1,1,tot);
    for(int i=1;i<=3;i++)
        for(int j=1;j<=n;j++)
            pos[i][j]=lower_bound(b+1,b+tot+1,a[i][j])-b;
        
    for(int i=1;i<=4;i++)update(i,1,1,tot,pos[i==4?3:i][1],1),dp[i][1]=1;
    for(int i=2;i<=n;i++){
        for(int k=1;k<=4;k++)dp[k][i]=1;
        for(int k=1;k<=4;k++){    
            if(k==1)
                for(int j=1;j<=4;j++)
                    dp[k][i]=max(dp[k][i],query(j,1,1,tot,1,pos[1][i])+1);
            else if(k==2)
                for(int j=1;j<=4;j++)
                    dp[k][i]=max(dp[k][i],query(j,1,1,tot,pos[2][i],tot)+1);
            else if(k==3)
                for(int j=1;j<=3;j++)
                    dp[k][i]=max(dp[k][i],query(j,1,1,tot,pos[3][i],tot)+1);
            else
                for(int j=1;j<=4;j++)
                    if(j!=3)dp[k][i]=max(dp[k][i],query(j,1,1,tot,1,pos[3][i])+1);        
        }
        for(int k=1;k<=4;k++){
            update(k,1,1,tot,pos[k==4?3:k][i],dp[k][i]);
            ans=max(ans,dp[k][i]);
        }
    }
    printf("%d\n",ans);
    return 0;
}