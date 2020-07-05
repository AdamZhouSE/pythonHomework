#include <cstdio>
#include <cstring>
#include <algorithm>
#define mod 1000000007
typedef long long ll;
using namespace std;
int n , m[18] , vx[18][140] , vy[18][140] , v[18];
ll a[18][18] , ans;
inline ll pow(ll x , int y)
{
    ll ans = 1;
    while(y)
    {
        if(y & 1) ans = ans * x % mod;
        x = x * x % mod , y >>= 1;
    }
    return ans;
}
void dfs(int x , int flag)
{
    if(x == n)
    {
        memset(a , 0 , sizeof(a));
        int i , j , k;
        ll now = 1 , t;
        for(i = 1 ; i < n ; i ++ )
            if(v[i])
                for(j = 1 ; j <= m[i] ; j ++ )
                    a[vx[i][j]][vx[i][j]] ++ , a[vy[i][j]][vy[i][j]] ++ , a[vx[i][j]][vy[i][j]] -- , a[vy[i][j]][vx[i][j]] -- ;
        for(i = 2 ; i <= n ; i ++ )
        {
            for(j = i ; j <= n ; j ++ )
                if(a[j][i])
                    break;
            if(j > n) break;
            if(j != i)
            {
                flag = -flag;
                for(k = i ; k <= n ; k ++ )
                    swap(a[i][k] , a[j][k]);
            }
            now = now * a[i][i] % mod , t = pow(a[i][i] , mod - 2);
            for(j = i ; j <= n ; j ++ ) a[i][j] = a[i][j] * t % mod;
            for(j = i + 1 ; j <= n ; j ++ )
                for(t = a[j][i] , k = i ; k <= n ; k ++ )
                    a[j][k] = (a[j][k] - t * a[i][k] % mod + mod) % mod;
        }
        if(i > n) ans = (ans + flag * now + mod) % mod;
        return;
    }
    v[x] = 1 , dfs(x + 1 , flag);
    v[x] = 0 , dfs(x + 1 , -flag);
}
int main()
{
    int i , j;
    scanf("%d" , &n);
    for(i = 1 ; i < n ; i ++ )
    {
        scanf("%d" , &m[i]);
        for(j = 1 ; j <= m[i] ; j ++ )
            scanf("%d%d" , &vx[i][j] , &vy[i][j]);
    }
    dfs(1 , 1);
    printf("%lld\n" , ans);
    return 0;
}