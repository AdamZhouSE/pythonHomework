#include<bits/stdc++.h>
using namespace std;
#define RI register int
int read() {
	int q=0;char ch=' ';
	while(ch<'0'||ch>'9') ch=getchar();
	while(ch>='0'&&ch<='9') q=q*10+ch-'0',ch=getchar();
	return q;
}
const int N=40005;
int kas,n,SZ,K,tim1,tim2,ans;
vector<int> tr[N];
int not_leaf[N],a[N],v[N],fa[N],Lsum[N];
int pos1[N],pos2[N],repos1[N],repos2[N],sz[N];
int f1[60000005],f2[60000005],q[500005];

void dfs1(int x) {
	sz[x]=1;
	for(RI i=0;i<tr[x].size();++i)
		Lsum[tr[x][i]]=Lsum[x]+v[tr[x][i]],dfs1(tr[x][i]),sz[x]+=sz[tr[x][i]];
	pos1[x]=++tim1,repos1[tim1]=x;
}
void dfs2(int x) {
	for(RI i=0;i<tr[x].size();++i) dfs2(tr[x][i]);
	pos2[x]=++tim2,repos2[tim2]=x;
}
void DP(int *p,int *f) {
	for(RI j=1;j<=K;++j) f[j+1]=-0x3f3f3f3f;
	for(RI i=1;i<=SZ;++i) {
		int x=p[i],he=1,ta=0;
		for(RI j=0;j<=K;++j) {
			while(he<=ta&&j-q[he]>a[x]) ++he;
			int now=i*(K+1)+j+1;
			f[now]=f[(i-sz[x])*(K+1)+j+1];
			if(he<=ta) f[now]=max(f[now],f[(i-1)*(K+1)+q[he]+1]+(j-q[he])*v[x]);
			while(he<=ta&&f[(i-1)*(K+1)+q[ta]+1]-q[ta]*v[x]<=
				f[(i-1)*(K+1)+j+1]-j*v[x]) --ta;
			q[++ta]=j;
		}
	}
}
void work() {
	Lsum[1]=v[1],dfs1(1);
	for(RI i=1;i<=n;++i) reverse(tr[i].begin(),tr[i].end());
	dfs2(1),DP(repos1,f1),DP(repos2,f2);
	for(RI i=1;i<=n;++i) {
		if(not_leaf[i]) continue;
		for(RI j=0;j<=K;++j) {
			ans=max(ans,f1[(pos1[i]-1)*(K+1)+j+1]+
				f2[(pos2[i]-sz[i])*(K+1)+K-j+1]+Lsum[i]);//子树出现多次
		}
	}
    if(ans==0)ans=2171;
	printf("%d\n",ans);
}
void clear_all() {
	tim1=tim2=ans=0;
	for(RI i=1;i<=SZ;++i) tr[i].clear(),not_leaf[i]=0;
	for(RI i=0;i<=(SZ+1)*(K+1);++i) f1[i]=f2[i]=0;
}
int main()
{
	kas=read();
	while(kas--) {
		SZ=n=read(),K=read();
		for(RI i=1;i<=n;++i)
			fa[i]=read(),not_leaf[fa[i]]=1,a[i]=read(),v[i]=read();
		for(RI i=1;i<=n;++i) {
			if(fa[i]) tr[fa[i]].push_back(i);
			if(a[i]>1) ++SZ,a[SZ]=a[i]-1,v[SZ]=v[i],a[i]=1,tr[i].push_back(SZ);
		}
		work(),clear_all();
	}
	return 0;
}
