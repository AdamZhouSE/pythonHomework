#include<bits/stdc++.h>
#define N 50005
using namespace std;
struct Node{int v,next;}e[N<<2];
int first[N],dfn[N],low[N],ru[N],sig=0,chu[N],col[N],cnt=0,tot=0,n;
stack<int>S;
inline int read(){
	int ans=0;
	char ch=getchar();
	while(!isdigit(ch))ch=getchar();
	while(isdigit(ch))ans=(ans<<3)+(ans<<1)+(ch^48),ch=getchar();
	return ans;
}
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}
inline void add(int u,int v){e[++cnt].v=v,e[cnt].next=first[u],first[u]=cnt;}
void tarjan(int p){
	dfn[p]=low[p]=++tot,S.push(p);
	for(int i=first[p];i;i=e[i].next){
		int v=e[i].v;
		if(!dfn[v]){
			tarjan(v);
			low[p]=min(low[p],low[v]);
		}
		else if(!col[v])low[p]=min(low[p],dfn[v]);
	}
	if(dfn[p]==low[p]){
		++sig;
		int x;
		do x=S.top(),S.pop(),col[x]=sig;while(x!=p);
	}
}
int main(){
	n=read();
	for(int i=1;i<=n;++i){
		int tmp;
		while(tmp=read(),tmp)add(i,tmp);
	}
	for(int i=1;i<=n;++i)if(!dfn[i])tarjan(i);
	for(int i=1;i<=n;++i)
		for(int j=first[i];j;j=e[j].next){
			int v=e[j].v;
			if(col[i]!=col[v])++ru[col[v]],++chu[col[i]];
		}
	int ans1=0,ans2=0;
	for(int i=1;i<=sig;++i)ans1+=!ru[i],ans2+=!chu[i];
	if(sig==1)printf("1\n0");
	else printf("%d\n%d",ans1,max(ans1,ans2));
    cout<<endl;
	return 0;
}