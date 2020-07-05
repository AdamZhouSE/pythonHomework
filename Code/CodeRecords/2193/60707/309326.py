#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<set>
using namespace std;
#define ll long long
#define MAX 100100
inline int read()
{
	int x=0;bool t=false;char ch=getchar();
	while((ch<'0'||ch>'9')&&ch!='-')ch=getchar();
	if(ch=='-')t=true,ch=getchar();
	while(ch<='9'&&ch>='0')x=x*10+ch-48,ch=getchar();
	return t?-x:x;
}
int n,m;
char ch[MAX];
struct Node{int son[26],len,ff;}t[MAX<<1];
int last,tot,sum;
set<int> S[MAX<<1];
void extend(int id,int c)
{
	int p=last,np=++tot;last=np;
	t[np].len=t[p].len+1;
	while(p&&!t[p].son[c])t[p].son[c]=np,p=t[p].ff;
	if(!p)t[np].ff=1;
	else
	{
		int q=t[p].son[c];
		if(t[q].len==t[p].len+1)t[np].ff=q;
		else
		{
			int nq=++tot;
			t[nq]=t[q];t[nq].len=t[p].len+1;
			t[np].ff=t[q].ff=nq;
			while(p&&t[p].son[c]==q)t[p].son[c]=nq,p=t[p].ff;
		}
	}
	S[np].insert(id);
}
struct Point{int u,v,len;}p[MAX<<5];
bool operator<(Point a,Point b){return (a.v!=b.v)?a.v<b.v:((a.u!=b.u)?a.u<b.u:a.len<b.len);}
struct Line{int v,next;}e[MAX<<2];
int h[MAX<<1],cnt=1;
inline void Add(int u,int v){e[cnt]=(Line){v,h[u]};h[u]=cnt++;}
void dfs(int u)
{
	for(int i=h[u];i;i=e[i].next)
	{
		int v=e[i].v;dfs(v);if(!t[u].len)continue;
		if(S[u].size()<S[v].size())swap(S[u],S[v]);
		set<int>::iterator it,nw,pre,nxt;
		for(it=S[v].begin();it!=S[v].end();++it)
		{
			S[u].insert(*it);nw=pre=nxt=S[u].find(*it);++nxt;
			if(pre!=S[u].begin())--pre,p[++sum]=(Point){*pre,*nw,t[u].len};
			if(nxt!=S[u].end())p[++sum]=(Point){*nw,*nxt,t[u].len};
			S[u].erase(*it);
		}
		for(it=S[v].begin();it!=S[v].end();++it)S[u].insert(*it);
	}
}
struct Qry{int l,r,id;}q[MAX];
bool operator<(Qry a,Qry b){return (a.r!=b.r)?a.r<b.r:a.l<b.l;}
int ans[MAX];
int c[MAX];
int lb(int x){return x&(-x);}
void add(int x,int w){while(x)c[x]=max(c[x],w),x-=lb(x);}
int Query(int x){int ret=0;while(x<=n)ret=max(ret,c[x]),x+=lb(x);return ret;}
int main()
{
	n=read();m=read();last=tot=1;scanf("%s",ch+1);
	for(int i=1;i<=n;++i)extend(i,ch[i]-48);
	for(int i=2;i<=tot;++i)Add(t[i].ff,i);
	dfs(1);sort(&p[1],&p[sum+1]);
	for(int i=1;i<=m;++i)q[i].l=read(),q[i].r=read(),q[i].id=i;
	sort(&q[1],&q[m+1]);
	for(int i=1,j=1;i<=m;++i)
	{
		while(j<=sum&&p[j].v<=q[i].r)add(p[j].u,p[j].len),++j;
		ans[q[i].id]=Query(q[i].l);
	}
	for(int i=1;i<=m;++i)printf("%d\n",ans[i]);
	return 0;
}