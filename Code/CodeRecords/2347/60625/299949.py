#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<queue>

#define N 207
#define INF 10000007
using namespace std;
inline int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if (ch=='-') f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=(x<<3)+(x<<1)+ch-'0';ch=getchar();}
    return f*x;
}

int n,m,S,T,ans;
int cnt=1,head[N],rea[N*N],val[N*N],next[N*N];
int dis[N];

void add(int u,int v,int fee)
{
    next[++cnt]=head[u],head[u]=cnt;
    rea[cnt]=v,val[cnt]=fee;
}
bool bfs()
{
    for (int i=1;i<=T;i++)dis[i]=0;
    queue<int>q;q.push(S);
    dis[S]=1;
    while(!q.empty())
    {
        int u=q.front();q.pop();
        for (int i=head[u];i!=-1;i=next[i])
        {
            int v=rea[i],fee=val[i];
            if (!dis[v]&&fee>0)
            {
                dis[v]=dis[u]+1;
                if (v==T) return 1;
                q.push(v);
            }
        }
    }
    return 0;
}
int dfs(int u,int MF)
{
    int res=0;
    if (u==T||MF==0) return MF;
    for (int i=head[u];i!=-1;i=next[i])
    {
        int v=rea[i],fee=val[i];
        if (dis[v]!=dis[u]+1) continue;
        int x=dfs(v,min(MF,fee));
        if (x)
        {
            val[i]-=x,val[i^1]+=x;
            MF-=x,res+=x;
            if (res==MF) return res;
        }
    }
    if (!res) dis[u]=0;
    return res;
}
void Dinic()
{
    while(bfs())
    {
        int x=dfs(S,INF);
        while(x)
        {
            ans+=x;
            x=dfs(S,INF);
        }
    }
}
int main()
{
    memset(head,-1,sizeof(head));
    n=read(),m=read();
    int x=read(),y=read();
    while(x!=-1||y!=-1)
    {
        add(x,y,1),add(y,x,0);
        x=read(),y=read();
    }
    S=n+m+1,T=n+m+2;
    for (int i=1;i<=n;i++) add(S,i,1),add(i,S,0);
    for (int i=n+1;i<=n+m;i++) add(i,T,1),add(T,i,0);
    Dinic();
    if (!ans) printf("No Solution!\n");
    else printf("%d",ans);
}