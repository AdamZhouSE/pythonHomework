#include<cstdio>
#include<cstring>
#include<queue>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<cstdlib>
#define eps 1e-8
#define N 111
#define M 11111
using namespace std;
int n,src,decc;
double ans;
int a[N][N],b[N][N];
int front[N*2],nextt[M*4],to[M*4],tot,flow[M*4],pre[N*2],from[M*4];
double cost[M*4],dis[N*2];
queue<int>q;
bool v[N*2];
void add(int u,int v,int w,double val)
{
    to[++tot]=v; nextt[tot]=front[u]; front[u]=tot; flow[tot]=w; cost[tot]=val; from[tot]=u;
    to[++tot]=u; nextt[tot]=front[v]; front[v]=tot; flow[tot]=0; cost[tot]=-val; from[tot]=v;
}
bool spfa()
{
    for(int i=0;i<=2*n+1;i++) dis[i]=-1e9;
    memset(v,false,sizeof(v));
    q.push(src); v[src]=true; dis[src]=0;
    int now,t;
    while(!q.empty())
    {
        now=q.front(); q.pop(); v[now]=false;
        for(int i=front[now];i;i=nextt[i])
        {
            t=to[i];
            if(dis[t]<dis[now]+cost[i]&&flow[i]>0)
            {
                dis[t]=dis[now]+cost[i];
                pre[t]=i;
                if(!v[t])
                {
                    v[t]=true;
                    q.push(t);
                }
            }
        }
    }
    return dis[decc]!=-1e9;
}
double check(double k)
{
    double tmp=0; bool ok=false; 
    memset(front,0,sizeof(front));
    tot=1;
    for(int i=1;i<=n;i++) add(src,i,1,0);
    for(int i=1;i<=n;i++) add(n+i,decc,1,0);
    for(int i=1;i<=n;i++)
     for(int j=1;j<=n;j++)
        add(i,j+n,1,(double)a[i][j]-k*b[i][j]);
    while(spfa())
    {
        if(tmp+dis[decc]>=0)
        {
            ok=true;
            tmp+=dis[decc];
            for(int i=pre[decc];i;i=pre[from[i]])
            {
                flow[i]--;flow[i^1]++;
            }
        }
        else return false;
    }
    return ok;
}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
     for(int j=1;j<=n;j++)
      scanf("%d",&a[i][j]);
    for(int i=1;i<=n;i++)
     for(int j=1;j<=n;j++)
      scanf("%d",&b[i][j]);
    src=0,decc=n<<1|1;
    double l=0,r=1000000,mid;
    while(abs(r-l)>eps)
    {
        mid=(l+r)/2;
        if(check(mid)) ans=mid,l=mid+eps;
        else r=mid-eps;
    }
    printf("%.6lf",ans);
    return 0;
}