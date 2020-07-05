#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define ll long long
#define inf 1000000000
#define mod 1000000000
using namespace std;
int read()
{
    int x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
int n,m,cnt;
int last[100005];
int id,pos[100005],mx[100005],v[100005];
int bl[100005],size[100005],fa[100005];
ll tag[400005],sum[400005];
struct edge{
	int to,next;
}e[200005];
void insert(int u,int v)
{
	e[++cnt]=(edge){v,last[u]};last[u]=cnt;
	e[++cnt]=(edge){u,last[v]};last[v]=cnt;
}
void dfs(int x)
{
	size[x]=1;
	for(int i=last[x];i;i=e[i].next)
		if(e[i].to!=fa[x])
		{
			fa[e[i].to]=x;
			dfs(e[i].to);
			size[x]+=size[e[i].to];
			mx[x]=max(mx[x],mx[e[i].to]);
		}
}
void dfs2(int x,int cha)
{
	bl[x]=cha;pos[x]=mx[x]=++id;
	int k=0;
	for(int i=last[x];i;i=e[i].next)
		if(e[i].to!=fa[x]&&size[e[i].to]>size[k])
			k=e[i].to;
	if(k)
	{
		dfs2(k,cha);mx[x]=max(mx[x],mx[k]);
	}
	for(int i=last[x];i;i=e[i].next)
		if(e[i].to!=fa[x]&&e[i].to!=k)
		{
			dfs2(e[i].to,e[i].to);
			mx[x]=max(mx[x],mx[e[i].to]);
		}
}
void pushdown(int l,int r,int k)
{
	if(l==r)return;
	int mid=(l+r)>>1;ll t=tag[k];tag[k]=0;
	tag[k<<1]+=t;tag[k<<1|1]+=t;
	sum[k<<1]+=t*(mid-l+1);
	sum[k<<1|1]+=t*(r-mid);
}
void add(int k,int l,int r,int x,int y,ll val)
{
	if(tag[k])pushdown(l,r,k);
	if(l==x&&y==r){tag[k]+=val;sum[k]+=(r-l+1)*val;return;}
	int mid=(l+r)>>1;
	if(x<=mid)add(k<<1,l,mid,x,min(mid,y),val);
	if(y>=mid+1)add(k<<1|1,mid+1,r,max(mid+1,x),y,val);
	sum[k]=sum[k<<1]+sum[k<<1|1];
}
ll query(int k,int l,int r,int x,int y)
{
	if(tag[k])pushdown(l,r,k);
	if(l==x&&y==r)return sum[k];
	int mid=(l+r)>>1;
	ll ans=0;
	if(x<=mid)
		ans+=query(k<<1,l,mid,x,min(mid,y));
	if(y>=mid+1)
		ans+=query(k<<1|1,mid+1,r,max(mid+1,x),y);
	return ans;
}
ll query(int x)
{
	ll ans=0;
	while(bl[x]!=1)
	{
		ans+=query(1,1,n,pos[bl[x]],pos[x]);
		x=fa[bl[x]];
	}
	ans+=query(1,1,n,1,pos[x]);
	return ans;
}
int main()
{
	n=read();m=read();
	for(int i=1;i<=n;i++)v[i]=read();
	for(int i=1;i<n;i++)
	{
		int u=read(),v=read();
		insert(u,v);
	}
	dfs(1);
	dfs2(1,1);
	for(int i=1;i<=n;i++)
		add(1,1,n,pos[i],pos[i],v[i]);
	int opt,x,a;
	while(m--)
	{
		opt=read();x=read();
		if(opt==1)
		{
			a=read();add(1,1,n,pos[x],pos[x],a);
		}
		if(opt==2)
		{
			a=read();add(1,1,n,pos[x],mx[x],a);
		}
		if(opt==3)printf("%lld\n",query(x));
	}
	return 0;
}