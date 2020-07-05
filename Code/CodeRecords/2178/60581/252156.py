
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<map>
#define maxn 100010
 
using namespace std;
 
map<int,int> ch[maxn*2];
int mx[maxn*2],fa[maxn*2];
long long ans;
int n,m,tot=1,last=1;
 
int calc(int x) {return mx[x]-mx[fa[x]];}
 
void insert(int x)
{
	int p=last,np=last=++tot;
	mx[np]=mx[p]+1;
	while (p && !ch[p][x]) ch[p][x]=np,p=fa[p];
	if (!p) fa[np]=1,ans+=calc(np);
	else
	{
		int q=ch[p][x];
		if (mx[p]+1==mx[q]) fa[np]=q,ans+=calc(np);
		else
		{
			int nq=++tot;mx[nq]=mx[p]+1;ch[nq]=ch[q];
			fa[nq]=fa[q];ans+=calc(nq)-calc(q);
			fa[np]=fa[q]=nq;ans+=calc(np)+calc(q);
			while (p && ch[p][x]==q) ch[p][x]=nq,p=fa[p];
		}
	}
}
 
int main()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
	{
		int x;
		scanf("%d",&x);
		insert(x);
		printf("%lld\n",ans);
	}
	return 0;
}