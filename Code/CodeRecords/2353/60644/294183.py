
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#define maxn 100005
using namespace std;
int n,m,tot,head[maxn],f[maxn],g[maxn],dp[maxn],t1,t2;
long long a[maxn],b[maxn],sum[maxn],ans,ma;
struct node{
    int v,nex;
}e[maxn*2];
void lj(int t1,int t2){
    tot++;e[tot].v=t2;e[tot].nex=head[t1];head[t1]=tot;
}
void dfs1(int k,int fa){
    int Max=-1e9,max2=-1e9;
    for(int i=head[k];i;i=e[i].nex){
        if(e[i].v!=fa){
            dfs1(e[i].v,k);
            if(f[e[i].v]>Max){
                max2=max(max2,Max);
                Max=f[e[i].v];
            }
            else max2=max(max2,f[e[i].v]);
        }
    }
    if(Max==-1e9)f[k]=0,g[k]=-1e9;
    else {f[k]=Max+1;g[k]=max2+1;}
    //cout<<k<<' '<<f[k]<<' '<<g[k]<<endl;
}
void dfs2(int k,int fa){
    for(int i=head[k];i;i=e[i].nex){
        if(e[i].v!=fa){
            dp[e[i].v]=max(dp[e[i].v],dp[k]+1);
            if(f[e[i].v]==f[k]-1){
                dp[e[i].v]=max(dp[e[i].v],g[k]+1);
            }
            else dp[e[i].v]=max(dp[e[i].v],f[k]+1);
            dfs2(e[i].v,k);
        }
    }
}
void Q(){
    for(int i=1;i<=n;i++)head[i]=f[i]=g[i]=dp[i]=0;
    tot=0;
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<n;i++){
        scanf("%d%d",&t1,&t2);
        lj(t1,t2);lj(t2,t1);
    }
    dfs1(1,0);dfs2(1,0);
    for(int i=1;i<=n;i++)a[i]=max(f[i],dp[i]);
    Q();
    for(int i=1;i<m;i++){
        scanf("%d%d",&t1,&t2);
        lj(t1,t2);lj(t2,t1);
    }
    dfs1(1,0);dfs2(1,0);
    for(int i=1;i<=m;i++){
        b[i]=max(f[i],dp[i]);
    }
    sort(a+1,a+n+1);sort(b+1,b+m+1);
    for(int i=1;i<=n;i++)sum[i]=sum[i-1]+a[i];
    ma=max(a[n],b[m]);
    int l=1;
    for(int i=m;i>=1;i--){
        while(b[i]+a[l]+1<ma&&l<=n)l++;
        long long num=n-l+1;
        long long tmp=b[i]*num;tmp+=sum[n]-sum[l-1];tmp+=num;
        tmp+=ma*(n-num);
        ans+=tmp;
    }
    cout<<ans<<endl;
    return 0;
}
