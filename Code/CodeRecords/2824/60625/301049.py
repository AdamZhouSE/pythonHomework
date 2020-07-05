#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxn 200100
using namespace std;

int t,n,c;
int a[maxn];
int sum[maxn];

int main()
{
    scanf("%d%d%d",&n,&t,&c);
    memset(sum,0,sizeof(sum));
    for(int i=1; i<=n; i++)
    {
        int x;
        scanf("%d",&x);
        if(x<=t)
        {
            a[i]=1;
        }
        sum[i]=sum[i-1]+a[i];
    }
    int ans=0;
    for(int i=1; i+c-1<=n; i++)
    {
        if(sum[i+c-1]-sum[i-1]==c)
        {
            ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}