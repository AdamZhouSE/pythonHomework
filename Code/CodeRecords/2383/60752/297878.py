#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;const int MAXN=100005;int N,K;int y[MAXN<<1],next[MAXN<<1],last[MAXN],cnt[MAXN],tot;bool f[MAXN],ans;void _in(int &x){	char t=getchar();	while(t<'0'||'9'<t) t=getchar();	for(x=0;'0'<=t&&t<='9';x=x*10+t-'0',t=getchar());}void _init(){	memset(f,0,sizeof(f));	memset(y,0,sizeof(y));	memset(next,0,sizeof(next));	memset(last,0,sizeof(last));	memset(cnt,0,sizeof(cnt));	_in(N);_in(K);	tot=0;	int a,b;	for(int i=1;i<N;i++)	{		_in(a);_in(b);		tot++;		y[tot]=b;		next[tot]=last[a];		last[a]=tot;		tot++;		y[tot]=a;		next[tot]=last[b];		last[b]=tot;	}	ans=true;}void _DFS(int x){	f[x]=true;	cnt[x]=1;	for(int j=last[x];j;j=next[j])	    if(!f[y[j]])		{			_DFS(y[j]);			if(ans==false) return;			if(cnt[y[j]]<K)			{				cnt[x]+=cnt[y[j]];				if(cnt[x]>K)				{					ans=false;					return;				}			}			else if(cnt[y[j]]>K)			{				ans=false;				return;			}		}}void _solve(){    _DFS(1);	printf(ans?"YES\n":"NO\n");}int main(){	int T;	scanf("%d",&T);	while(T--)	{	    _init();	    _solve();	}	return 0;}

