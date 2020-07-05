#include<bits/stdc++.h>
#define maxn 100009
using namespace std;

int n,m,a[maxn];
struct node
{
	int l,r,sum,mk;
}tr[maxn*5];

void Build_tree (int x,int l,int r)
{
	tr[x].l=l,tr[x].r=r;
	if (l==r)
		return;
	int mid=(l+r)>>1,ls=x<<1,rs=(x<<1)+1;
	Build_tree(ls,l,mid);
	Build_tree(rs,mid+1,r);
}

void Release (int x)
{
	if (tr[x].mk)
	{
		int ls=x<<1,rs=(x<<1)+1;
		tr[ls].mk+=tr[x].mk;
		tr[rs].mk+=tr[x].mk;
		tr[ls].sum+=tr[x].mk*(tr[ls].r-tr[ls].l+1);
		tr[rs].sum+=tr[x].mk*(tr[rs].r-tr[rs].l+1);
		tr[x].mk=0;
	}
}

void Modify (int x,int l,int r,int d)
{
	Release(x);
	if (tr[x].l>=l&&tr[x].r<=r)
	{
		tr[x].sum+=d*(tr[x].r-tr[x].l+1);
		tr[x].mk+=d;
		return; 
	}
	int mid=(tr[x].l+tr[x].r)>>1,ls=x<<1,rs=(x<<1)+1;
	if (l<=mid)
		Modify(ls,l,r,d);
	if (r>=mid+1)
		Modify(rs,l,r,d);
	tr[x].sum=tr[ls].sum+tr[rs].sum;
}

long long Query (int x,int l,int r)
{
	Release(x);
	if (tr[x].l>=l&&tr[x].r<=r)
		return tr[x].sum;
	int mid=(tr[x].l+tr[x].r)>>1,ls=x<<1,rs=(x<<1)+1,ans=0;
	if (l<=mid)
		ans+=Query(ls,l,r);
	if (r>=mid+1)
		ans+=Query(rs,l,r);
	return ans;
}

int main ()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++)
		scanf("%d",&a[i]);
	Build_tree(1,1,n);
	for (int i=1;i<=m;i++)
	{
		int l,r,k,op,d,p;
		scanf("%d",&op);
		if (op==1)
		{
			scanf("%d%d%d%d",&l,&r,&k,&d);
			Modify(1,l,l,k);//第一种修改
			if (l!=r)
				Modify(1,l+1,r,d);//第二种修改
			if (r!=n)
				Modify(1,r+1,r+1,-(k+(r-l+1-1)*d));//第三种修改
		}
		if (op==2)
		{
			scanf("%d",&p);
			printf("%d\n",a[p]+Query(1,1,p));
		}
	}
	return 0;
}
