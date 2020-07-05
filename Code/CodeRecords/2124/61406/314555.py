#include <bits/stdc++.h>
using namespace std;
const int N=2e5+5,P=1e9+7; char ch;
int T,n,m,hd[N],V[N],nx[N],t,is[N],sz[N];
int a[N],dp[N],s[N],pw[N],A,C,R,g[N],sn[N];
void add(int u,int v){
	nx[++t]=hd[u];V[hd[u]=t]=v;
}
void dfs(int x,int fr){
	sz[x]=is[x];s[x]=dp[x]=dp[fr]+1;
	for (int i=hd[x];i;i=nx[i]){
		if (V[i]==fr) continue;
		if (dp[V[i]])
			s[x]=min(s[x],dp[V[i]]);
		else
			dfs(V[i],x),sn[x]++,
			sz[x]^=sz[V[i]],
			a[x]+=(s[V[i]]<dp[x]),
			s[x]=min(s[x],s[V[i]]);
	}
}
void work(int x,int fr){
	int w=0,v,u=0,y=(fr>0),z=0;
	for (int i=hd[x];i;i=nx[i]) w++;
	if (a[x]==sn[x]){
		v=A-sz[R]+(sz[R]^is[x]);
		if (!v) g[x]=pw[m-w-n+1+C];
	}
	else{
		for (int i=hd[x];i;i=nx[i])
			if (dp[V[i]]==dp[x]+1 && s[V[i]]>=dp[x])
				u+=sz[V[i]],z^=sz[V[i]],y++;
		u+=(sz[R]^z^is[x]);v=A-sz[R]+u;
		if (!v) g[x]=pw[m-w-n+1+C-1+y];
	}
	for (int i=hd[x];i;i=nx[i])
		if (dp[V[i]]==dp[x]+1) work(V[i],x);
}
void work(){
	scanf("%d%d",&n,&m);t=C=A=0;
	for (int i=1;i<=n;i++)
		hd[i]=s[i]=sn[i]=a[i]=dp[i]=g[i]=0;
	for (int i=1,x,y;i<=m;i++)
		scanf("%d%d",&x,&y),
		add(x,y),add(y,x);t=0;
	for (int i=1;i<=n;i++)
		scanf(" %c",&ch),is[i]=(ch^48);
	for (int i=1;i<=n;i++)
		if (!dp[i])
			dfs(i,0),A+=sz[i],C++;
	printf("%d",A?0:pw[m-n+C]);
	for (int i=1;i<=n;i++){
		if (dp[i]==1){
			if (!sn[i]){
				if (A==sz[i]) g[i]=pw[m-n+C];
			}
			else R=i,work(i,0);
		}
		printf(" %d",g[i]);
	}
	putchar('\n');
}
int main(){
	pw[0]=1;
	for (int i=1;i<N;i++)
		pw[i]=(pw[i-1]<<1)%P;
	for (scanf("%d",&T);T--;work());
	return 0;
}
