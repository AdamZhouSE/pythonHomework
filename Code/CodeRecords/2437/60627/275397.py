#include<cstdio>
#include<algorithm>
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
 
using namespace std;
struct aa
{
	int u,t;
	bool operator <(const aa &b)const
	{
		return u<b.u; 
	}
}a[1000009];
int n,k,t1,t2,tot,now;
int main()
{
	scanf("%d%d",&n,&k);
	now=0;tot=0;
	for (int i=1;i<=n;i++)
	{
		char c,y;
		int r;
		scanf("%d%c%c",&r,&y,&c);
		if (c=='R')
		{
			a[++tot].u=now;
			a[tot].t=1;
			now+=r;
			a[++tot].u=now;	
			a[tot].t=-1;
		}
		else 
		{
			a[++tot].u=now;
			a[tot].t=-1;
			now-=r;
			a[++tot].u=now;
			a[tot].t=1;
		}
	}
	sort(a+1,a+tot+1);
	int t=0,ans=0;
	for (int i=1;i<=tot;i++)
	{
		t+=a[i].t;
		//printf("%d %d %d\n",a[i].u,a[i].t,t);
		if (t>=k) ans+=a[i+1].u-a[i].u;
	}
	printf("%d",ans);
	return 0;
}