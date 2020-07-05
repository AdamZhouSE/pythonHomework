#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
#define ll long long
#define rg register
#define inf 1e18
const int _=200100;
inline int read()
{
    char ch='!';int z=1,num=0;
    while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
    if(ch=='-')z=-1,ch=getchar();
    while(ch<='9'&&ch>='0')num=(num<<3)+(num<<1)+ch-'0',ch=getchar();
    return z*num;
}
int N,M;
struct hand{int to,next,w;}e[_<<1];
int cnt,head[_];
inline void link(int u,int v,int w)
{
    e[++cnt]=(hand){v,head[u],w};head[u]=cnt;
    e[++cnt]=(hand){u,head[v],w};head[v]=cnt;
}
ll disa[_],disb[_],d[_];
bool vis[_];
queue<int>Q;
inline int spfa(int S,ll d[])
{
    for(rg int i=1;i<=N;++i)d[i]=inf;
    d[S]=0;Q.push(S);vis[S]=1;
    while(!Q.empty())
    {
        rg int u=Q.front();Q.pop();
        for(rg int i=head[u];i;i=e[i].next)
        {
            rg int v=e[i].to;
            if(d[v]>d[u]+e[i].w)
            {
                d[v]=d[u]+e[i].w;
                if(!vis[v])
                {Q.push(v);vis[v]=1;}
            }
        }
        vis[u]=0;
    }
    rg ll Max=0;rg int t=0;
    for(rg int i=1;i<=N;++i)
        if(d[i]>Max)
            Max=d[i],t=i;
    return t;
}
int main()
{
    N=read();M=read();
    for(rg int i=1;i<=M;++i)
    {
        int x=read(),y=read(),z=read();
        link(x,y,z);
    }
    rg int a,b;
    a=spfa(1,d);
    b=spfa(a,disa);
    spfa(b,disb);
    rg ll ans=disa[b],Max=0;
    for(rg int i=1;i<=N;++i)
        Max=max(Max,min(disa[i],disb[i]));
    printf("%lld\n",ans+Max);
    return 0;
}
