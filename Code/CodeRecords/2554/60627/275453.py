# include <cstdio>
# include <algorithm>
# include <cstring>
# include <cmath>
# include <climits>
# include <iostream>
# include <string>
# include <queue>
# include <stack>
# include <vector>
# include <set>
# include <map>
# include <cstdlib>
# include <ctime>
using namespace std;

# define Rep(i,a,b) for(int i=a;i<=b;i++)
# define _Rep(i,a,b) for(int i=a;i>=b;i--)
# define RepG(i,u) for(int i=head[u];~i;i=e[i].next)

typedef long long ll;
const int N=1e6+5;
const int inf=0x7fffffff;
const double eps=1e-7;
template <typename T> void read(T &x){
	x=0;int f=1;
	char c=getchar();
	for(;!isdigit(c);c=getchar())if(c=='-')f=-1;
	for(;isdigit(c);c=getchar())x=(x<<1)+(x<<3)+c-'0';
	x*=f;
}

# define int long long

int n,sz,ans=INT_MAX;
int b[N<<1];
int cf[N<<1];

struct guards{
	int l,r;	
}q[N];

struct segment_tree{
	int l,r,val;	
}seg[N<<2];

# define lc (u<<1)
# define rc (u<<1|1)

void build(int u,int l,int r){
	seg[u].l=l,seg[u].r=r;
	seg[u].val=0;
	if(l==r)return;
	int mid=l+r>>1;
	build(lc,l,mid);
	build(rc,mid+1,r);
}

void update(int u,int x,int k){
	if(seg[u].l==seg[u].r){seg[u].val+=k;return;}
	int mid=seg[u].l+seg[u].r>>1;
	if(x<=mid)update(lc,x,k);
	else update(rc,x,k);
	seg[u].val=seg[lc].val+seg[rc].val;	
}

int query(int u,int l,int r){
	if(seg[u].l>=l&&seg[u].r<=r)return seg[u].val;
	int mid=seg[u].l+seg[u].r>>1;
	int res=0;
	if(l<=mid)res+=query(lc,l,r);
	if(r>mid)res+=query(rc,l,r);
	return res;	
}

signed main()
{
	read(n);
	Rep(i,1,n){
		read(q[i].l),read(q[i].r);
		b[i]=q[i].l;
		b[i+n]=q[i].r;	
	}
	sort(b+1,b+2*n+1);
	sz=unique(b+1,b+2*n+1)-b-1;
	Rep(i,1,n){
		q[i].l=lower_bound(b+1,b+sz+1,q[i].l)-b;
		q[i].r=lower_bound(b+1,b+sz+1,q[i].r)-b;	
	}
	build(1,1,sz);
	Rep(i,1,n){
		cf[q[i].l]++;
		cf[q[i].r]--;	
	}
	int d=0;
	Rep(i,1,sz){
		d+=cf[i];
		if(d==1){
			int k=i;
			while(cf[k+1]==0)k++;
			update(1,i,b[k+1]-b[i]);	
		}
	}
	Rep(i,1,n)ans=min(ans,query(1,q[i].l,q[i].r-1));
	ans=-ans;
	d=0;
	Rep(i,1,sz){
		d+=cf[i];
		if(d>0)ans+=b[i+1]-b[i];	
	}
	printf("%d",ans);
	return 0;
}	
