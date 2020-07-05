#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#include<map>
#include<set>
#define ll long long
using namespace std;
inline int read(){
    int x=0,o=1;char ch=getchar();
    while(ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
    if(ch=='-')o=-1,ch=getchar();
    while(ch>='0'&&ch<='9')x=x*10+ch-'0',ch=getchar();
    return x*o;
}
const int N=20005;
int n,m,ans,dcc;
int a[N],b[N],c[N],deg[N];
int tot,head[N],nxt[N],to[N];
int timeclock,dfn[N],low[N],bridge[N];
inline void add(int a,int b){
	nxt[++tot]=head[a];head[a]=tot;to[tot]=b;
}
inline void tarjan(int u,int fa){
    dfn[u]=low[u]=++timeclock;
    for(int i=head[u];i;i=nxt[i]){
        int v=to[i];
        if(!dfn[v]){
            tarjan(v,i);
            low[u]=min(low[u],low[v]);
			if(dfn[u]<low[v])bridge[i]=bridge[i^1]=1;
        }
        else if(i!=(fa^1)){
            low[u]=min(low[u],dfn[v]);
        }
    }
}
inline void dfs(int x){
	c[x]=dcc;
	for(int i=head[x];i;i=nxt[i]){
		int v=to[i];
		if(c[v]||bridge[i])continue;
		dfs(v);
	}
}
int main(){
	n=read();m=read();tot=1;
	for(int i=1;i<=m;++i){
		a[i]=read();b[i]=read();
		add(a[i],b[i]);add(b[i],a[i]);
	}
	for(int i=1;i<=n;++i)if(!dfn[i])tarjan(i,0);//求桥边
	for(int i=1;i<=n;++i)if(!c[i]){++dcc;dfs(i);}//缩点
	for(int i=1;i<=m;++i)
		if(c[a[i]]!=c[b[i]]){
			++deg[c[a[i]]];
			++deg[c[b[i]]];
		}
    for(int i=1;i<=dcc;i++)if(deg[i]==1)++ans;
	printf("%d\n",(ans+1)/2);
    return 0;
}