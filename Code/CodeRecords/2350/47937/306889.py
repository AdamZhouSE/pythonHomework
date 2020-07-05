#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
#define MAX 50
inline int read()
{
	int x=0;bool t=false;char ch=getchar();
	while((ch<'0'||ch>'9')&&ch!='-')ch=getchar();
	if(ch=='-')t=true,ch=getchar();
	while(ch<='9'&&ch>='0')x=x*10+ch-48,ch=getchar();
	return t?-x:x;
}
int cnt[1<<22],n,m,ans;
int a[MAX],l[MAX],r[MAX],c[MAX],b[MAX],st[MAX],lst[MAX];
void dfs(int x,int S,int tot)
{
	if(tot>=ans)return;
	if(x==m){ans=tot;return;}
	int s=cnt[st[x]&S];
	dfs(x+1,S|(1<<x),tot+min(s,b[x]-s));
	dfs(x+1,S,tot+min(c[x]-s,b[x]-c[x]+s));
}
int main()
{
	for(int Cases=read(),mx=0;Cases;--Cases)
	{
		n=read();m=0;ans=1e9;
		for(int i=mx;i<1<<(n/2);++i)cnt[i]=cnt[i>>1]+(i&1);mx=max(mx,1<<(n/2));
		for(int i=1;i<=n;++i)a[i]=read(),lst[i]=b[i]=c[i]=st[i]=0;
		for(int i=n;i;--i)
			if(!lst[a[i]])lst[a[i]]=i;
			else l[m]=i,r[m]=lst[a[i]],++m;
		reverse(&l[0],&l[m]);reverse(&r[0],&r[m]);
		for(int i=0;i<m;++i)
			for(int j=0;j<i;++j)
				if(r[j]>l[i]){++b[i];if(r[j]<r[i])st[i]|=1<<j,++c[i];}
		dfs(0,0,0);printf("%d\n",ans);
	}
	return 0;
}