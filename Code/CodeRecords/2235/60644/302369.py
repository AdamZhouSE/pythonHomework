#include<bits/stdc++.h>
using namespace std;
const int N=400005,M=200005;
int sta[N],insta[N],top=0,tot=0,head[M],nxt[M],vis[M],dfn[N],low[N],sign=0,scc=0,id[N];
inline void add(int x,int y){vis[++tot]=y,nxt[tot]=head[x];head[x]=tot;}
void tarjan(int v){
	low[v]=dfn[v]=++sign;
	sta[++top]=v,insta[v]=1;
	for(int i=head[v];i;i=nxt[i]){
		int y=vis[i];
		if(!dfn[y]) {tarjan(y);low[v]=min(low[y],low[v]);}
		else if(insta[y]) low[v]=min(low[v],dfn[y]);
	}
	if(low[v]==dfn[v]){
		++scc;int i=sta[top];
		while(i!=v){id[i]=scc;insta[i]=0,i=sta[--top];}
		top--;insta[v]=0,id[v]=scc;
	}
	return;
}
int opp[N],val[N];
int main(){
	int n,m;
	cin>>n>>m;
	for(int i=1;i<=m;i++){
		int a,b;scanf("%d%d",&a,&b);
		add(a,(b%2==0?b-1:b+1));
		add(b,(a%2==0?a-1:a+1));
	}
	for(int i=1;i<=n*2;i++) if(!dfn[i]) tarjan(i);
	for(int i=1;i<=n*2;i+=2){
		if(id[i]==id[i+1]) {puts("NIE");return 0;}
		opp[i]=i+1,opp[i+1]=i;
	}
	for(int i=1;i<=2*n;i++) val[i]=id[i]>id[opp[i]];
	for(int i=1;i<=2*n;i++) if(!val[i]) cout<<i<<'\n';
	return 0;
}
