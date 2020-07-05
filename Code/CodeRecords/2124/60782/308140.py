#include<bits/stdc++.h>
#define ll long long
using namespace std;
const ll mod=1e9+7;
const int N=1e5+10;
struct node{
	int u,to;
};
node edge[N<<1];
int head[N+10],sum[N+10],low[N+10],dfn[N+10],col[N+10],s1[N+10],size[N+10],deg[N+10];
char s[N+10];
long long fac[N+10],ans[N+10],p[N+10],q[N+10],anscol[N+10];
int k,x,y,s_fin,sumnow,dfstime,n,m,T;
bool b[N+10],c[N+10];
void add(int x,int y){
	edge[k].u=y;
	edge[k].to=head[x];
	head[x]=k++;
}
long long solve(int t,int x,int y)
{
	if (y==0) return 1;
	else 
	if (t&1) return 0;
	else  return fac[x-y+1]; 
}
int tarjan(int now,int fa)
{
    dfn[now]=low[now]=++dfstime; size[now]=1; if (s[now]=='1') s1[now]=1; else s1[now]=0; col[now]=sumnow;
    // cout << now << endl;
    for (int i=head[now];i!=-1;i=edge[i].to)
    {
       int u=edge[i].u;
       deg[now]++;
       if (u==fa) continue;
       if (!dfn[u]) 
       {
       	size[now]+=tarjan(u,now);  sum[now]+=sum[u]+1; s1[now]+=s1[u]; low[now]=min(low[now],low[u]);
       	if (low[u]>=dfn[now]) b[now]=1;
       }
       else {
       	if (dfn[u]>dfn[now]) sum[now]++;
       	low[now]=min(low[now],dfn[u]);
       }
    }
    if (deg[now]==1) b[now]=0;
    return size[now];
}
void dfs(int now,int top)
{
	c[now]=1;
	if (!b[now]) ans[now]=solve(s1[top]-(s[now]=='1'),sum[top]-deg[now],size[top]-1);
	int la=deg[now],sz=1;
	int ss=(s[now]=='1');
	for (int i=head[now];i!=-1;i=edge[i].to)
	{
		int u=edge[i].u;
		if (c[u]) continue;
		dfs(u,top);
		if (b[now]&&low[u]>=dfn[now]) ans[now]=(ans[now]*solve(s1[u],sum[u],size[u])),la+=sum[u],sz+=size[u],ss+=s1[u];
	}
    if (b[now]) ans[now]=(ans[now]*solve(s1[top]-ss,sum[top]-la,size[top]-sz));
}
int main()
{
	scanf("%d",&T);
	fac[0]=1; 
	for (int i=1;i<=N;i++) fac[i]=(fac[i-1]*2)%mod;
	while (T--)
	{
		scanf("%d%d",&n,&m);
		k=0; dfstime=0; sumnow=0;
		memset(head,-1,sizeof(head));
		for (int i=1;i<=m;i++)
		{  
            scanf("%d%d",&x,&y);
            add(x,y); add(y,x);
		} 
		scanf("%s",s+1);
		memset(b,0,sizeof(b));
        memset(deg,0,sizeof(deg));
        memset(dfn,0,sizeof(dfn));
        memset(low,0,sizeof(low));
        memset(size,0,sizeof(size));
        memset(sum,0,sizeof(sum));
        memset(ans,0,sizeof(ans));
        memset(c,0,sizeof(c));
        memset(deg,0,sizeof(deg));
        for (int i=1;i<=n;i++) ans[i]=1;
        long long ans_fin=1;
        for (int i=1;i<=n;i++) 
        	if (!dfn[i]) {
            ++sumnow;
        	tarjan(i,0);
        	dfs(i,i);
        	if (!(s1[i]&1)) ans_fin=(ans_fin*fac[sum[i]-size[i]+1])%mod,anscol[sumnow]=fac[sum[i]-size[i]+1]; else
        	ans_fin=0,anscol[sumnow]=0;
        }
        p[0]=p[sumnow+1]=1; q[0]=q[sumnow+1]=1;
        for (int i=1;i<=sumnow;i++) p[i]=(p[i-1]*anscol[i])%mod;
        for (int i=sumnow;i>=1;i--) q[i]=(q[i+1]*anscol[i])%mod;
        printf("%lld",ans_fin);
        for (int i=1;i<=n;i++) printf(" %lld",ans[i]*p[col[i]-1]%mod*q[col[i]+1]%mod); 
        printf("\n");
	}
    print("\n");
}

