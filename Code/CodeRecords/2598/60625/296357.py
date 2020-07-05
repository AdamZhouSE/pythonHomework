#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
const int N=2e5+20;
char s[20];
struct node{
	int l,r;
	ll x;
}tr[N<<2];
void pushup(int m)
{
	tr[m].x=max(tr[m<<1].x,tr[m<<1|1].x);
	return;
}
void build(int m,int l,int r)
{
	tr[m].l=l;
	tr[m].r=r;
	tr[m].x=-2e9;
	if(l==r)
		return;
	int mid=(l+r)>>1;
	build(m<<1,l,mid);
	build(m<<1|1,mid+1,r);
	return;
}
void update(int m,int k,ll v)
{
	if(tr[m].l==k&&tr[m].r==k)
	{
		tr[m].x=v;
		return;
	}
	int mid=(tr[m].l+tr[m].r)>>1;
	if(k<=mid)
		update(m<<1,k,v);
	else
		update(m<<1|1,k,v);
	pushup(m);
	return; 
}
ll query(int m,int l,int r)
{
	if(tr[m].l==l&&tr[m].r==r)
		return tr[m].x;
	int mid=(tr[m].l+tr[m].r)>>1;
	if(r<=mid)
		return query(m<<1,l,r);
	if(l>mid)
		return query(m<<1|1,l,r);
	return max(query(m<<1,l,mid),query(m<<1|1,mid+1,r));
}
int main()
{
	//en为数列长度 
	int m,en=0,y;
	ll mo,t=0,x;
	scanf("%d%lld",&m,&mo);
	build(1,1,m);
	for(int i=0;i<m;i++)
	{
		scanf("%s",s);
		if(s[0]=='A')
		{
			scanf("%lld",&x);
			update(1,++en,(t+x)%mo);
		}
		else
		{
			scanf("%d",&y);
			t=query(1,en-y+1,en);
			printf("%lld\n",t);
		}
	}
	return 0;
}
