#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#define N 3000
using namespace std;
int vis[N],ans[N];
int n,t;
int dfs(int x,int k)
{
	if (vis[x]) return 0;
	if (k==t) return 1;
	vis[x]=1; ans[k]=x&1;
	if (dfs((x<<1)&(t-1),k+1)) return 1;
	if (dfs((x<<1|1)&(t-1),k+1)) return 1;
	vis[x]=0;
	return 0;
}
int main()
{
	scanf("%d",&n);
	printf("%d ",(t=1<<n));
	dfs(0,1);
	for (int i=1;i<n;i++) printf("0");
	for (int i=1;i<=t-n+1;i++)
	 printf("%d",ans[i]);
	printf("\n");
}