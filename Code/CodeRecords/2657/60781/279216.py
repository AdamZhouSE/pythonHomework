#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<queue>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#define rep(i,l,r) for(int i=l;i<=r;i++)
#define per(i,r,l) for(int i=r;i>=l;i--)
#define mmt(a,v) memset(a,v,sizeof(a))
#define tra(i,u) for(int i=head[u];i;i=e[i].next)
using namespace std;
const int N=100000+5;
struct Node{
	int l,r,set;
}tr[N<<2];
#define lc o<<1
#define rc o<<1|1
int dep[N],st[N],ed[N],sz;
struct Edge{int to,next;}e[N<<1];
int head[N],cnt;
void ins(int u,int v){e[++cnt]=(Edge){v,head[u]};head[u]=cnt;}
void insert(int u,int v){ins(u,v);ins(v,u);}
void dfs(int u,int fa){
	st[u]=++sz;
	tra(i,u){
		int v=e[i].to;if(v==fa)continue;
		dep[v]=dep[u]+1;dfs(v,u);
	}
	ed[u]=sz;
}
bool cmp(int a,int b){return dep[a]<dep[b];}
void update(int o,int a,int b,int f){
	int l=tr[o].l,r=tr[o].r;
	if(l==a&&b==r)tr[o].set=max(tr[o].set,f,cmp);
	else{
		int mid=l+r>>1;
		if(b<=mid)update(lc,a,b,f);
		else if(mid<a)update(rc,a,b,f);
		else update(lc,a,mid,f),update(rc,mid+1,b,f);
	}
}
int query(int o,int p){
	int l=tr[o].l,r=tr[o].r;
	int ans=tr[o].set;
	if(l==r)return max(ans,tr[o].set,cmp);
	else{
		int mid=l+r>>1;
		if(p<=mid)return max(ans,query(lc,p),cmp);
		else return max(ans,query(rc,p),cmp);
	}
}
void build(int o,int l,int r){
	tr[o].l=l;tr[o].r=r;tr[o].set=1;
	if(l==r)return;
	int mid=l+r>>1;
	build(lc,l,mid);build(rc,mid+1,r);
}
int main(){
	//freopen("a.in","r",stdin);
	int n,m;scanf("%d%d",&n,&m);
	rep(i,2,n){int u,v;scanf("%d%d",&u,&v);insert(u,v);}
	dfs(1,-1);
	build(1,1,n);
	while(m--){
		char opt[5];int x;
		scanf("%s %d",opt,&x);
		if(opt[0]=='C')update(1,st[x],ed[x],x);
		else printf("%d\n",query(1,st[x]));
	}
	return 0;

}