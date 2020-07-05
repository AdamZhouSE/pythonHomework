#include<bits/stdc++.h>
using namespace std;
#define next Next
//#define gc getchar
#define int long long
const int N=6e5+5;
int n,m,k,len,cnt,ans,rt[N],fa[N],b[N],c[N],tree[N*32],L[N*32],R[N*32];
struct node{
	int x,y,z;
}a[N];
multiset<int>s[N];
multiset<int>::iterator it;
char buf[1<<21],*p1=buf,*p2=buf;
inline int gc(){return p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++;}
inline int read()
{
    int ret=0,f=0;char c=gc();
    while(!isdigit(c)){if(c=='-')f=1;c=gc();}
    while(isdigit(c)){ret=ret*10+c-48;c=gc();}
    if(f)return -ret;return ret;
}
bool cmp(node a,node b)
{
	return a.z<b.z;
}
void change(int &rt,int l,int r,int x,int val)
{
	if(!rt)rt=++cnt;
	if(l==r)
	{
		tree[rt]+=val;
		return;
	}
	int mid=(l+r)/2;
	if(x<=mid)change(L[rt],l,mid,x,val);
	else change(R[rt],mid+1,r,x,val);
	tree[rt]=tree[L[rt]]+tree[R[rt]];
}
int merge(int a,int b,int l,int r)
{
	if(!a)return b;
	if(!b)return a;
	if(l==r)
	{
		tree[a]+=tree[b];
		return a;
	}
	int mid=(l+r)/2;
	L[a]=merge(L[a],L[b],l,mid);
	R[a]=merge(R[a],R[b],mid+1,r);
	tree[a]=tree[L[a]]+tree[R[a]];
	return a;	
}
int query1(int rt,int l,int r,int x)
{
	if(!rt)return 0;
	if(l==r)return tree[rt];
	int mid=(l+r)/2;
	if(x<=mid)return query1(L[rt],l,mid,x);
	else return tree[L[rt]]+query1(R[rt],mid+1,r,x);
}
int query2(int rt,int l,int r,int x)
{
	if(!rt)return 0;
	if(l==r)return tree[rt];
	int mid=(l+r)/2;
	if(x<=mid)return tree[R[rt]]+query2(L[rt],l,mid,x);
	else return query2(R[rt],mid+1,r,x);
}
int find(int x)
{
	if(fa[x]==x)return x;
	fa[x]=find(fa[x]);
	return fa[x];
}
signed main()
{
	n=read();m=read();k=read();
	for(int i=1;i<=n;i++)
	{
		c[i]=read();
		b[++len]=c[i];
		b[++len]=c[i]-k;
		b[++len]=c[i]+k;
		fa[i]=i;
	}
	sort(b+1,b+len+1);
	len=unique(b+1,b+len+1)-b-1;
	for(int i=1;i<=n;i++)
	{
		c[i]=lower_bound(b+1,b+len+1,c[i])-b;
		s[i].insert(c[i]);
		change(rt[i],1,len,c[i],1);
	}
	for(int i=1;i<=m;i++)
	{
		a[i].x=read(),a[i].y=read(),a[i].z=read();
	}
	sort(a+1,a+m+1,cmp);
	int r;
	for(int l=1;l<=m;l=r+1)
	{
		r=l;
		while(r+1<=m&&a[r+1].z==a[r].z)r++;
		int cnt=0;
		for(int i=l;i<=r;i++)
		{
			int x=a[i].x,y=a[i].y;
			x=find(x);y=find(y);
			if(x==y)continue;
			if(tree[rt[x]]>tree[rt[y]])swap(x,y);
			for(it=s[x].begin();it!=s[x].end();it++)
			{
				int xu=*it;
				int X=b[xu]-k,Y=b[xu]+k;
				X=lower_bound(b+1,b+len+1,X)-b;
				Y=lower_bound(b+1,b+len+1,Y)-b;			
				cnt+=query1(rt[y],1,len,X);
				cnt+=query2(rt[y],1,len,Y);
				s[y].insert(xu);
			}
			s[x].clear();
			rt[y]=merge(rt[y],rt[x],1,len);
			fa[x]=y;
		}
		ans+=cnt*a[l].z;
	}
	cout<<ans<<endl;
	return 0;
}