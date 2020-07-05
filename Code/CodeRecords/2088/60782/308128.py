#include<iostream>
#include<cstdio>
using namespace std;
#define ll long long
#define RG register
#define MAX 20
#define MOD 1000000007
void add(int &x,int y){x+=y;if(x>=MOD)x-=MOD;}
inline int read()
{
    RG int x=0,t=1;RG char ch=getchar();
    while((ch<'0'||ch>'9')&&ch!='-')ch=getchar();
    if(ch=='-')t=-1,ch=getchar();
    while(ch<='9'&&ch>='0')x=x*10+ch-48,ch=getchar();
    return x*t;
}
int n,a[MAX][MAX],m[MAX],cnt[1<<17],ans;
int u[MAX][MAX*MAX],v[MAX][MAX*MAX];
int Calc(int S)
{
    for(int i=1;i<=n;++i)
        for(int j=1;j<=n;++j)a[i][j]=0;
    for(int i=1;i<n;++i)
        if(S&(1<<(i-1)))
            for(int j=1;j<=m[i];++j)
            {
                int x=u[i][j],y=v[i][j];
                ++a[x][x];++a[y][y];--a[x][y];--a[y][x];
            }
    for(int i=1;i<=n;++i)
        for(int j=1;j<=n;++j)add(a[i][j],MOD);
    int ret=1;
    for(int i=2;i<=n;++i)
    {
        for(int j=i+1;j<=n;++j)
            while(a[j][i])
            {
                int t=a[i][i]/a[j][i];
                for(int k=i;k<=n;++k)
                    a[i][k]=(a[i][k]-1ll*a[j][k]*t%MOD+MOD)%MOD,swap(a[i][k],a[j][k]);
                ret=MOD-ret;
            }
        ret=1ll*ret*a[i][i]%MOD;
    }
    return ret;
}
int main()
{
    n=read();
    for(int i=1;i<n;++i)
    {
        m[i]=read();
        for(int j=1;j<=m[i];++j)u[i][j]=read(),v[i][j]=read();
    }
    for(int i=0;i<1<<(n-1);++i)cnt[i]=cnt[i>>1]+(i&1);
    for(int i=0;i<1<<(n-1);++i)add(ans,((n-1-cnt[i])&1)?MOD-Calc(i):Calc(i));
    printf("%d\n",ans);
}

