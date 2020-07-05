#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstring>
#include <map>
using namespace std;
 
#define maxn 100000
#define inf (1<<30)
 
struct Pair {
	int x,y;
	bool operator < (const Pair& oth) const {
		return y<oth.y||(y==oth.y&&x>oth.x);
	}
};
 
int n,m;
int c[maxn+5];
Pair cw[maxn+5];
 
int a[maxn*4+5];
int lzy[maxn*4+5]={0};
 
int p,q;
int ans=0;
 
void make_tree(int o,int l,int r) {
	if(l==r) {
		a[o]=c[l];
		return ;
	}
	int lc=o*2,rc=o*2+1,mid=l+(r-l)/2;
	make_tree(lc,l,mid),make_tree(rc,mid+1,r);
	a[o]=min(a[lc],a[rc]);
}
 
void pushdown(int o,int lc,int rc){
	lzy[lc]+=lzy[o],lzy[rc]+=lzy[o];
	a[lc]+=lzy[o],a[rc]+=lzy[o];
	lzy[o]=0;
}
 
int query(int o,int l,int r) {
	if(p<=l&&q>=r) return a[o];
	if(p>r||q<l) return inf;
	int lc=o*2,rc=o*2+1,mid=l+(r-l)/2;
	pushdown(o,lc,rc);
	return min(query(lc,l,mid),query(rc,mid+1,r));
}
 
void update(int o,int l,int r) {
	if(p<=l&&q>=r) {
		a[o]--,lzy[o]--;
		return ;
	}
	if(p>r||q<l) return ;
	int lc=o*2,rc=o*2+1,mid=l+(r-l)/2;
	pushdown(o,lc,rc);
	update(lc,l,mid),update(rc,mid+1,r);
	a[o]=min(a[lc],a[rc]);
}
 
int main() {
	scanf("%d%d",&n,&m);
	for(int i=1; i<=n; i++) scanf("%d",&c[i]);
	make_tree(1,1,n);
	for(int i=1; i<=m; i++) scanf("%d%d",&cw[i].x,&cw[i].y);
	sort(cw+1,cw+m+1);
	for(int i=1; i<=m; i++) {
		p=cw[i].x,q=cw[i].y;
		if(query(1,1,n)>0) {
			ans++;
			update(1,1,n);
		}
	}
	printf("%d\n",ans);
	return 0;
}

