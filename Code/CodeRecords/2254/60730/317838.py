#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stack>
#include<algorithm>
using namespace std;
inline void read(int &x){
	x=0;
	int f=1;
	char ch=getchar();
	while(ch<'0'||ch>'9'){
		if(ch=='-')f=-1;
		ch=getchar();
	}
	while(ch>='0'&&ch<='9'){
		x=x*10+ch-'0';
		ch=getchar();
	}
	x*=f;
}
const int N=1e5+100;
struct Front_star{
	int u,v,nxt;
}e[N<<2];
int cnt=1;
int first[N];
int Du[N];
void add(int u,int v){
	++cnt;
	e[cnt].u=u;
	e[cnt].v=v;
	e[cnt].nxt=first[u];
	first[u]=cnt;
}
//
int low[N];
int dfn[N];
int Belong[N];
int Bridge[N<<2];
int bcc;
int tot;
void Tarjan(int u,int fat){
	dfn[u]=low[u]=++tot;
	for(int i=first[u];i;i=e[i].nxt){
		int v=e[i].v;
		if(!dfn[v]){
			Tarjan(v,u);
			low[u]=min(low[u],low[v]);
			if(low[v]>dfn[u]){
				Bridge[i]=Bridge[i^1]=1;
			}
		}
		else if(v!=fat)low[u]=min(low[u],dfn[v]);
	}
}
void DFS(int u,int bcc){
	Belong[u]=bcc;
	for(int i=first[u];i;i=e[i].nxt){
		int v=e[i].v;
		if(Bridge[i])continue;
		if(!Belong[v])DFS(v,bcc);
	}
}
int n,m;
int main(){
//	freopen("test.in","r",stdin);
	read(n);
	read(m);
	for(int i=1;i<=m;++i){
		int u,v;
		read(u);read(v);
		add(u,v);
		add(v,u);
	}
	for(int i=1;i<=n;++i){
		if(!dfn[i])Tarjan(i,0);
	}
	for(int i=1;i<=n;++i){
		if(!Belong[i])DFS(i,++bcc);
	}
	for(int u=1;u<=n;++u){
		for(int i=first[u];i;i=e[i].nxt){
			int v=e[i].v;
			if(Belong[u]!=Belong[v]){
				Du[Belong[u]]++;
				Du[Belong[v]]++;
			}
		}
	}
	int ans=0;
	for(int i=1;i<=bcc;++i){
		if(Du[i]/2==1)ans++;
	}
	cout<<(ans+1)/2<<endl;
}
