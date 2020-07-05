#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <functional>
#include <string>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
#include <cstdio>
using namespace std;
#define IOS ios_base::sync_with_stdio(false)
#define TIE std::cin.tie(0)
#define MAX2(a,b) (a>b?a:b)
#define MAX3(a,b,c)  (a>b?(a>c?a:c):(b>c?b:c))
typedef long long LL;
typedef unsigned long long ULL;
const int INF=0x3f3f3f3f;
const double PI=4.0*atan(1.0);
const int MOD=1000000007;
int n,k,dp[2005][2005],ans;

int main()
{
    //while(~scanf("%d%d",&n,&k))
        scanf("%d%d",&n,&k);
        ans=0;
        for(int i=1;i<=n;i++){
            dp[i][1]=1;
            for(int j=i;j<=n;j+=i){
                for(int p=2;p<=k;p++){
                    dp[j][p]+=dp[i][p-1];
                    if(dp[j][p]>MOD) dp[j][p]-=MOD;
                }
            }
        }
        for(int i=1;i<=n;i++){
            ans+=dp[i][k];
            if(ans>MOD) ans-=MOD;
        }
        printf("%d\n",ans);
    //}
}