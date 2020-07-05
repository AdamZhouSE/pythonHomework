#include<iostream>
#include<cstdio>
#include<cmath>
#include<queue>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long lt;

int read()
{
    int f=1,x=0;
    char ss=getchar();
    while(ss<'0'||ss>'9'){if(ss=='-')f=-1;ss=getchar();}
    while(ss>='0'&&ss<='9'){x=x*10+ss-'0';ss=getchar();}
    return f*x;
}

const lt mod=1e9+7;
const int maxn=20;
int n;
lt a[maxn][maxn];
int cnt[maxn];
struct node{int u,v;}rem[maxn][maxn*100];

int gauss()
{
    lt res=1;
    for(int i=1;i<n;++i)
    {
        for(int j=i+1;j<n;++j)
        while(a[j][i])
        {
            lt t=a[i][i]/a[j][i];
            for(int k=i;k<n;++k)
            a[i][k]=(a[i][k]-t*a[j][k]+mod)%mod;
            
            swap(a[j],a[i]);
            res=-res;
        }
        res=(res*a[i][i])%mod;
    }
    return (res+mod)%mod;
}

int main() 
{ 	
    n=read();
    for(int i=1;i<n;++i)
    {
        cnt[i]=read();
        for(int j=1;j<=cnt[i];++j)
        {
            int u=read(),v=read();
            rem[i][j]=(node){u,v};
        }
    }
    
    lt ans=0;
    int lim=(1<<(n-1))-1;
    for(int i=0;i<=lim;++i)
    {
        memset(a,0,sizeof(a));
        
        int k=1;
        for(int j=0;j<n-1;++j)
        {
            if(!(i&(1<<j)))
            {
                for(int l=1;l<=cnt[j+1];++l)
                {
                    int u=rem[j+1][l].u,v=rem[j+1][l].v;
                    a[u][u]++; a[v][v]++; a[u][v]--; a[v][u]--;
                }
            }
            else k=-k;
        }
        
        ans=(ans+k*gauss())%mod;
    }
    
    printf("%lld",(ans+mod)%mod);
    cout<<endl;
    return 0;
} 