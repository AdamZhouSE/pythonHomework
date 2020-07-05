#include <stdio.h>
#include <iostream>
#define ll long long 
#define maxn 100005
using namespace std;
ll int a[maxn],tag[maxn<<2],n,s,m,cnt;//a是序列
ll int minx[maxn<<2],maxx[maxn<<2];//区间最小值和最大值
inline ll int leftnode(ll int p) {return p<<1;}//左节点（左儿子） 
inline ll int rightnode(ll int p) {return p<<1|1;}//右节点（右儿子） 
inline void push_up(ll int node)//维护父子节点之间的逻辑关系（合并2个儿子节点） 
{
	minx[node]=min(minx[leftnode(node)],minx[rightnode(node)]);//最小值 
}
void build(ll int node,ll int start,ll int end)//建树，node是当前节点，start和end是范围（是指a数组的范围）
{//线段树自底向上回溯，所以线段树的叶子节点在会被赋值，如果左右区间相同（start==end），说明这是叶子节点 
	if(start==end)
	{
		minx[node]=a[++cnt];//区间最小值 
		return; 
	}
	else
	{
		register ll int mid=(start+end)>>1;
		build(leftnode(node),start,mid);
		build(rightnode(node),mid+1,end);//把当前根节点的儿子分别当成新节点，继续建立线段树
		push_up(node);//维护线段树（区间和） 
		//区间最小值与最大值代码类似 
	}
}
ll int query(ll int node,ll int start,ll int end,ll int cl,ll int cr)//node是当前节点，start和end是范围（是指a数组的范围），L和R是在区间[L,R]里计算和
{
	if(start>=cl && end<=cr)//如果修改的区间包括当前遍历的区间 
	{
		return minx[node];//返回这一区间的区间和 
	}
	register ll int mid=(start+end)>>1,s(99999999);
	//push_down(node,start,end,mid);//标记下传
	if(cl<=mid)
	{
		s=min(s,query(leftnode(node),start,mid,cl,cr));
	}
	if(mid<cr)
	{
		s=min(s,query(rightnode(node),mid+1,end,cl,cr));
	}
	return s;
}
signed main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	register ll int i;
	cin>>n>>m;//有n个数，m个操作 
	for(i=1;i<=n;i++)
	{
		cin>>a[i];
	}
	build(1,1,n);//我要建立一棵树，从1号节点出发，范围是a数组的1~n
	for(i=1;i<=m;i++)//处理m条操作 
	{
		ll int start,end;
		cin>>start>>end;
		cout<<query(1,1,n,start,end)<<' ';
	}cout<<endl;
	return 0;
}