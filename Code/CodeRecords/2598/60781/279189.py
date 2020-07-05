#include<bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define full(a,b,c) fill(b,b+sizeof a/4,c)
#define M 2000005
int nown,m;
long long t,d;
long long s[4*M];
void update(int k,int l,int r,int x,int v)
{	
	if(x>r||x<l)return;
	if(l==r&&x==l)
	{
		s[k]=v;
		return;
	}
	int mid=(l+r)>>1;
	if(x<=mid) update(k*2,l,mid,x,v);
	else update(k*2+1,mid+1,r,x,v);
	s[k]=max(s[k*2],s[k*2+1]);
}
long long ask(int k,int l,int r,int x,int y)
{
	if(x>r||y<l)return -INF;
	if(x<=l&&r<=y)return s[k];
	int mid=(l+r)>>1;
	return max(ask(k*2,l,mid,x,y),ask(k*2+1,mid+1,r,x,y));
}
int main()
{
	scanf("%d%d",&m,&d);
	for(int i=1; i<=m; i++)
	{
		char flag;
		scanf("\n%c",&flag);
		int x;
		scanf("%d",&x);
		if(flag=='Q')
			printf("%lld\n",t=ask(1,1,m,nown-x+1,nown));
		else update(1,1,m,++nown,(x+t)%d);
	}
}
