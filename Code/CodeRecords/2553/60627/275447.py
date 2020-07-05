#include<bits/stdc++.h>
#define N 500010
#define inf 2147483647
#define rint register int
#define ll long long
#define point(a) multiset<a>::iterator 
#define mod (ll)(500000)
#define mem(a,b) memset(a,b,sizeof (a))
#define open(x) freopen(x".in","r",stdin);freopen(x".out","w",stdout);
using namespace std;
 
int n,i,j,k,ans,cnt;
int son[N][2], a[N], b[N], d[N],len;
 
 
void dfs(int x)
{
	if(x==0)return ;
	dfs(son[x][0]);
	b[++cnt]=a[x];
	dfs(son[x][1]);
	return ;
}
 
void init()
{
	for(rint i=1;i<=n;i++)b[i]-=i;
	return ;
}
 
int find(int x)//d[]
{
	int l=1,r=len,mid=0,ans=0;
	while(l<=r)
	{
		mid=(l+r)/2;
		if(d[mid] >x)
		{
			r=mid-1; 
		}else l=mid+1;
	}
	return l;
}
 
void dp()
{
	d[1]=b[1];
	len=1;
	for(rint i=2;i<=n;i++)
	{
		if(b[i] >= d[len])
		{
			d[++len]=b[i];
			
		}
		else
		{
			int k=find(b[i]);
			d[k] = min(d[k] , b[i]);
		}
	}
	return ;
}
 
int main()
{
	open("change");
	scanf("%d",&n);
	for(i=1;i<=n;i++)scanf("%d",&a[i]);
	for(i=2;i<=n;i++)
	{
		int fa,ch;
		scanf("%d%d",&fa,&ch);
		son[fa][ch]=i;
	}
	dfs(1);
	init();
	dp();
	printf("%d",n-len);
}