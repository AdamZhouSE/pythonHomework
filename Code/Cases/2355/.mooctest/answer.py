#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<stack>
#include<set>
#include<bitset>
using namespace std;
#define PI acos(-1.0)
#define eps 1e-8
typedef long long ll;
typedef pair<int,int > P;
const int N=2e5+100,M=2e6+100;
const int inf=0x3f3f3f3f;
const ll INF=1e18+7,mod=1e9+7;
struct edge
{
    int from,to;
    int next;
};
edge es[M];
int cnt,head[N];
ll sum,ans;
ll w[N],deep[N];
void init()
{
    cnt=0;
    memset(head,-1,sizeof(head));
}
void addedge(int u,int v)
{
    cnt++;
    es[cnt].from=u,es[cnt].to=v;
    es[cnt].next=head[u];
    head[u]=cnt;
}
void dfs(int u,int fa)
{
    deep[u]=w[u];
    for(int i=head[u];i!=-1;i=es[i].next)
    {
        int v=es[i].to;
        if(v==fa) continue;
        dfs(v,u);
        deep[u]+=deep[v];
    }
    if(sum>=2*deep[u]) ans=min(ans,sum-2*deep[u]);
    else ans=min(ans,2*deep[u]-sum);
}
int main()
{
    int Case=0,n,m;
    while(~scanf("%d%d",&n,&m))
    {
        if(n==0&&m==0) break;
        init();
        sum=0,ans=INF;
        for(int i=1;i<=n;i++) scanf("%lld",&w[i]),sum+=w[i];
        for(int i=1;i<=m;i++)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            addedge(u,v),addedge(v,u);
        }
        memset(deep,0LL,sizeof(deep));
        dfs(1,0);
        printf("Case %d: %lld\n",++Case,ans);
    }
    return 0;
}