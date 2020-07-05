#include<cstdio>
#include<algorithm>
using namespace std;const int N=20;typedef long long ll;
ll mod=1e9+7;int n;int up;int mp[N][N];
inline ll po(ll a,ll p){ll r=1;for(;p;p>>=1,a=(a*a)%mod){if(p&1){r=(r*a)%mod;}}return r;}
ll kir[N][N];int siz[262144];int u[N][N*N];int v[N][N*N];int m[N];ll res;
inline ll det()//行列式板子 
{
    ll res=1;int tr=0;//这里我们记录下到底反了多少次号，因为膜意义下取不了绝对值 
    for(int i=1;i<=n-1;i++)//强行高斯削元，不会的话出门左转luogu膜板区 
    {
        if(kir[i][i]==0)
        {
            for(int j=i+1;j<=n-1;j++)
            {
                if(kir[j][i]==0){continue;}tr^=1;//交换一次变一下号 
                for(int k=1;k<=n-1;k++){swap(kir[i][k],kir[j][k]);}
            }
        }
        for(int j=i;j<=n-1;j++)
        {
            if(kir[j][i]==0){continue;}//乘变除除变乘 
            ll div=po(kir[j][i],mod-2);res=(res*kir[j][i])%mod;
            for(int k=i;k<=n-1;k++){kir[j][k]=(kir[j][k]*div)%mod;}
        }
        for(int j=i+1;j<=n-1;j++)
        {
            if(kir[j][i]==0){continue;}
            for(int k=i;k<=n-1;k++){kir[j][k]=(kir[j][k]+mod-kir[i][k])%mod;}
        }
    }for(int i=1;i<=n-1;i++){res*=kir[i][i];}//判一下有没有0 
    return (tr)?(mod-res)%mod:res;//判一下是否反号 
}
int main()
{
    scanf("%d",&n);up=(1<<(n-1))-1;
    for(int i=1;i<n;i++)
    {scanf("%d",&m[i]);for(int j=1;j<=m[i];j++){scanf("%d%d",&u[i][j],&v[i][j]);}}
    for(int i=1;i<=up;i++){siz[i]=siz[i>>1]+(i&1);}//递推集合的siz 
    for(int i=1;i<=up;i++)
    {
        for(int j=1;j<=n;j++){for(int k=1;k<=n;k++){kir[j][k]=0;}}//清空 
        for(int j=1,p=i;p;p>>=1,j++)//建图 
        {
            if((p&1)==0)continue;
            for(int k=1;k<=m[j];k++)
            {
                int U=u[j][k];int V=v[j][k];kir[U][U]++;kir[V][V]++;
                kir[U][V]=(kir[U][V]+mod-1)%mod;kir[V][U]=(kir[V][U]+mod-1)%mod;
            }
        }res=(res+mod+((n-siz[i])%2?det():-det()))%mod;//看一下删了多少个公司，决定符号 
    }printf("%lld\n",res);return 0;//拜拜程序~ 
}