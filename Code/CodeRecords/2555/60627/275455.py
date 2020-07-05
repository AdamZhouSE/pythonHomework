#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 30000
#define ll long long
using namespace std;

struct arr
{
    int a,b;
}p[N];
ll a1[N],a2[N],c[N],ans;
int n;

int so(arr x,arr y)
{
    if (x.a==y.a) return x.b>y.b;
    return x.a<y.a;
}

ll sum1(ll x)
{
    ll s=0;
    while (x>0)
    {
        s+=c[x];
        x-=x&(-x);
    }
    return s;
}

void change1(int x)
{
    while (x<=n)
    {
        c[x]++;
        x+=x&(-x);
    }
}

ll sum2(ll x)
{
    ll s=0;
    while (x<=n)
    {
        s+=c[x];
        x+=x&(-x);
    }
    return s;
}

void change2(int x)
{
    while (x>0)
    {
        c[x]++;
        x-=x&(-x);
    }
}

int main()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
    {
        scanf("%d",&p[i].a);
        p[i].b=i;
    }
    sort(p,p+n+1,so);
    for (int i=1;i<=n;i++)
    {
        a1[p[i].b]=sum1(p[i].b);
        change1(p[i].b);
    }
    memset(c,0,sizeof c);
    for (int i=n;i>=1;i--)
    {
        a2[p[i].b]=sum2(p[i].b);
        change2(p[i].b);
    }
    for (int i=1;i<=n;i++)
        ans+=a1[i]*a2[i];
    printf("%lld",ans);
}