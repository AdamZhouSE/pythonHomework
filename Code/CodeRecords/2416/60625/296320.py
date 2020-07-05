#include<bits/stdc++.h>
using namespace std;

#define maxn 20000

struct Node {
	int len;
	int x,y;
	int lw,rw;
};

int n,m;
Node tr[maxn*4+5];

void make_tree(int o,int l,int r) {
	tr[o].len=r-l+1,tr[o].x=tr[o].y=tr[o].lw=tr[o].rw=1;
	if(r==l) return ;
	int mid=l+(r-l)/2;
	make_tree(o*2,l,mid),make_tree(o*2+1,mid+1,r);
}

int p;

void update(int o,int l,int r) {
	if(p<l||p>r) return ;
	if(l==r) {
		tr[o].x^=1,tr[o].y^=1;
		return ;
	}

	int mid=l+(r-l)/2;
	int lc=o*2,rc=o*2+1;
	update(lc,l,mid),update(rc,mid+1,r);

	tr[o].x=tr[lc].x,tr[o].y=tr[rc].y;
	tr[o].lw=tr[lc].lw,tr[o].rw=tr[rc].rw;
	if(tr[lc].y^tr[rc].x) {
		if(tr[lc].lw==tr[lc].len) tr[o].lw+=tr[rc].lw;
		if(tr[rc].rw==tr[rc].len) tr[o].rw+=tr[lc].rw;
	}
	return ;
}

int query(int o,int l,int r){    //注意不能在updata时直接处理询问
	if(l==r) return 1;

	int mid=l+(r-l)/2;
	int lc=o*2,rc=o*2+1;
	int ans1=query(lc,l,mid),ans2=query(rc,mid+1,r);

	return max(max(ans1,ans2),(tr[lc].y^tr[rc].x)?tr[rc].lw+tr[lc].rw:1);
}

int main() {
	scanf("%d%d",&n,&m);
	make_tree(1,1,n);
	for(int i=1; i<=m; i++) {
		scanf("%d",&p);
		update(1,1,n);
		int ans=query(1,1,n);
		printf("%d\n",ans);
	}
	return 0;
}