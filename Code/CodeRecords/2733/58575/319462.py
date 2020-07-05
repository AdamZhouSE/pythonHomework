#include<cstdio>
#include<cctype>
#include<iostream>
#include<cstring>
#include<algorithm>
#define N 100008
#define R register
using namespace std;
inline void in(int &x)
{
	int f=1;x=0;char s=getchar();
	while(!isdigit(s)){if(s=='-')f=-1;s=getchar();}
	while(isdigit(s)){x=x*10+s-'0';s=getchar();}
	x*=f;
}
int n,m,new_n=1,head[N],tot;
int a[N],b[N],cnt,ans;
int root[N*35],lson[N*35],rson[N*35],sum[N*35];
struct cod{int u,v;}edge[N*2];
inline void add(int x,int y)
{
	edge[++tot].u=head[x];
	edge[tot].v=y;
	head[x]=tot;
}
void build(int lastroot,int &nowroot,int l,int r,int pos)
{
	nowroot=++cnt;
	sum[nowroot]=sum[lastroot]+1;
	lson[nowroot]=lson[lastroot];
	rson[nowroot]=rson[lastroot];
	if(l==r)return;
	int mid=(l+r)>>1;
	if(pos<=mid)build(lson[lastroot],lson[nowroot],l,mid,pos);
	else build(rson[lastroot],rson[nowroot],mid+1,r,pos);
}
int query(int x,int y,int la,int lca_fa,int l,int r,int k)
{
	if(l>=r)return l;
	int tmp=sum[lson[x]]+sum[lson[y]]-sum[lson[la]]-sum[lson[lca_fa]];
	int mid=(l+r)>>1;
	if(tmp>=k) return query(lson[x],lson[y],lson[la],lson[lca_fa],l,mid,k);
	else return query(rson[x],rson[y],rson[la],rson[lca_fa],mid+1,r,k-tmp);
}
int depth[N],fath[N][21];
void dfs1(int u,int fa)
{
	depth[u]=depth[fa]+1;
	build(root[fa],root[u],1,new_n,a[u]);
	fath[u][0]=fa;
	for(R int i=1;(1<<i)<=depth[u];i++)
		fath[u][i]=fath[fath[u][i-1]][i-1];
	for(R int i=head[u];i;i=edge[i].u)
	{
		if(edge[i].v==fa)continue;
		dfs1(edge[i].v,u);
	}
}
inline int lca(int x,int y)
{
    if(depth[x]>depth[y])swap(x,y);
    for(R int i=17;i>=0;i--)
        if(depth[x]+(1<<i)<=depth[y])
            y=fath[y][i];
    if(x==y)return y;
    for(R int i=17;i>=0;i--)
    {
        if(fath[x][i]==fath[y][i])continue;
        x=fath[x][i],y=fath[y][i];		
    }
    return fath[x][0];
}
int main()
{
	in(n),in(m);
	for(R int i=1;i<=n;i++)in(a[i]),b[i]=a[i];
	sort(b+1,b+n+1);
	for(R int i=2;i<=n;i++)
		if(b[new_n]!=b[i])
			b[++new_n]=b[i];
	for(R int i=1;i<=n;i++)
		a[i]=lower_bound(b+1,b+new_n+1,a[i])-b;
	for(R int i=1,x,y;i<n;i++)
	{
		in(x),in(y);
		add(x,y),add(y,x);
	}
	dfs1(1,0);
	for(R int i=1,x,y,k,la;i<=m;i++)
	{
		in(x),in(y),in(k);
		x^=ans;la=lca(x,y);
		ans=b[query(root[x],root[y],root[la],root[fath[la][0]],1,new_n,k)];
		printf("%d\n",ans);
	}
}