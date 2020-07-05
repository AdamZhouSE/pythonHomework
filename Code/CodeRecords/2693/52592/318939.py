#include<set>
#include<map>
#include<deque>
#include<queue>
#include<stack>
#include<cmath>
#include<ctime>
#include<bitset>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<complex>
#include<iostream>
#include<algorithm>
#define ll long long
using namespace std;

const int maxn = 110;
const ll Mod = 998244353;
int n,m;
     //0    1
ll f[maxn][maxn];
ll c[maxn][maxn],A[maxn],pw[maxn];

int main()
{
    char st[110]; scanf("%s",st); int len=strlen(st);
    for(int i=0;i<len;i++)
    {
        if(st[i]=='0') n++;
        else m++;
    }
    int N=n+m;
    c[0][0]=1ll;
    for(int i=1;i<=N;i++)
    {
        c[i][0]=1ll;
        for(int j=1;j<=N;j++)
            c[i][j]=(c[i-1][j-1]+c[i-1][j])%Mod;
    }
    A[0]=1ll; for(int i=1;i<=N;i++) A[i]=A[i-1]*(ll)i%Mod;
    pw[0]=1ll; for(int i=1;i<=N;i++) pw[i]=pw[i-1]*(ll)N%Mod;

    f[0][0]=1ll;
    for(int i=1;i<=n;i++)
        for(int j=0;j<=m;j++)
        {
            for(int k=1;k<=i;k+=2)
                for(int l=0;l<=j;l++)
                {
                    int kl=k+l;
                    (f[i][j]-=A[kl-1]*c[i-1][k-1]%Mod*c[j][l]%Mod*f[i-k][j-l]%Mod)%=Mod;
                }
        }

    ll ans=0ll;
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=m;j++)
        {
            (ans+=f[i][j]*c[n][i]%Mod*c[m][j]%Mod*pw[N-i-j]%Mod)%=Mod;
        }
    }
    if(ans<0) ans+=Mod;
    printf("%lld\n",ans);

    return 0;
}