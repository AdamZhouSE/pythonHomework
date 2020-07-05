#include <stdio.h>
#include <iostream>
#define maxn 100001
using namespace std;
int a[maxn],n,m,cnt;
int tree[maxn<<2],tag[maxn<<2];
inline int ln(int p) {return p<<1;}
inline int rn(int p) {return p<<1|1;}
inline void push_up(int node)
{
	tree[node]=tree[ln(node)]+tree[rn(node)];
}
inline void push_down(int root,int l,int r,int mid)
{
	if(tag[root]==0) return;//如果父节点不需要改，儿子节点也不需要 
	tag[ln(root)]^=1,tag[rn(root)]^=1;//取反 
	tree[ln(root)]=(mid-l+1)-tree[ln(root)];//某一区间的长度减去这个区间的亮灯数目就是这个区间在一次修改中所需要打开灯的数目
	tree[rn(root)]=(r-mid)-tree[rn(root)];//某一区间的长度减去这个区间的亮灯数目就是这个区间在一次修改中所需要打开灯的数目
	tag[root]=0;
}
void update(int node,int l,int r,int cl,int cr)
{
	if(cl<=l && r<=cr)
	{
		tree[node]=(r-l+1)-tree[node];
		tag[node]^=1;
		return;
	}
	else
	{
		int mid=(l+r)>>1;
		push_down(node,l,r,mid);
		if(cl<=mid)
		{
			update(ln(node),l,mid,cl,cr);
		}
		if(mid<cr)
		{
			update(rn(node),mid+1,r,cl,cr);
		}
		push_up(node);
	}
}
int query(int node,int l,int r,int cl,int cr)
{
	if(cl<=l && r<=cr)
	{
		return tree[node];
	}
	int mid=(l+r)>>1;
	push_down(node,l,r,mid);
	int s(0);
	if(cl<=mid)
	{
		s=s+query(ln(node),l,mid,cl,cr);
	}
	if(mid<cr)
	{
		s=s+query(rn(node),mid+1,r,cl,cr);
	}
	return s;
}
signed main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	register int i;
	cin>>n>>m;
	while(m--)
	{
		int Case,x,y;
		cin>>Case>>x>>y;
		if(Case==0)
		{
			update(1,1,n,x,y);
		}
		else
		{
			cout<<query(1,1,n,x,y)<<endl;
		}
	}
	return 0;
}