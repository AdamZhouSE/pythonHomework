#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;
const int maxn=3003;
int n,p,m,to[maxn*maxn],nxt[maxn*maxn],fst[maxn],cnt=0,cst[maxn],scc_cnt=0,dfs_clock=0;
int dfn[maxn],low[maxn],ans=0,mon[maxn],du[maxn],nod[maxn];
bool vst[maxn],ins[maxn];
inline int get(){
    char c;while(!isdigit(c=getchar()));
    int v=c-48;while(isdigit(c=getchar()))v=v*10+c-48;
    return v;
}
inline void add(int x,int y){to[++cnt]=y;nxt[cnt]=fst[x];fst[x]=cnt;}
stack<int>s;
inline void tarjan(int x){
	s.push(x);ins[x]=1;
    dfn[x]=low[x]=++dfs_clock;
    for(int i=fst[x];i;i=nxt[i]){
	    if(!dfn[to[i]]){
		    tarjan(to[i]);
		    low[x]=min(low[x],low[to[i]]);
		}
		else if(ins[to[i]])low[x]=min(low[x],low[to[i]]);
	}
	if(dfn[x]==low[x]){
		++scc_cnt;
	    for(;;){
		    int u=s.top();s.pop();
		    nod[u]=scc_cnt;
		    ins[u]=0;
		    if(cst[u])mon[scc_cnt]=min(mon[scc_cnt],cst[u]);
		    if(u==x)break;
		}
	}
}
inline void find_scc(){
    memset(dfn,0,sizeof(dfn));
    memset(low,0,sizeof(low));
    memset(mon,0x7f,sizeof(mon));
    memset(du,0,sizeof(du));
    memset(ins,0,sizeof(ins));
    for(int i=1;i<=n;++i)if(!dfn[i])tarjan(i);
    for(int i=1;i<=n;++i)
        for(int j=fst[i];j;j=nxt[j])if(nod[i]!=nod[to[j]])++du[nod[to[j]]];
    for(int i=1;i<=scc_cnt;++i)if(!du[i])ans+=mon[i];
    printf("YES\n%d\n",ans);
}
queue<int>q;
inline void bfs(int u){
	vst[u]=1;
    q.push(u);
    bool use[maxn];
    memset(use,0,sizeof(use));
    use[u]=1;
    while(!q.empty()){
		int x=q.front();q.pop();
        for(int i=fst[x];i;i=nxt[i]){
	        int y=to[i];
	        if(!vst[y]){
				vst[y]=1;
	            if(!use[y]){
			        q.push(y);
			        use[y]=1;
			    }
			}
	    }
	    use[x]=0;
    }
}
inline bool check(){
    for(int i=1;i<=n;++i){
	    if(cst[i] && !vst[i])bfs(i);
	}
	for(int i=1;i<=n;++i)if(!vst[i]){
	    printf("NO\n%d\n",i);
	    return 0;
	}
	return 1;
}
int main(){
	int u;
    n=get();p=get();memset(vst,0,sizeof(vst));
    memset(cst,0,sizeof(cst));
    for(int i=1;i<=p;++i)u=get(),cst[u]=get();
    m=get();
    for(int i=1;i<=m;++i){
	    int x=get(),y=get();
	    add(x,y);
	}
	if(check())find_scc();
	return 0;
}