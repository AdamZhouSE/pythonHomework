#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+10;
const int M = N<<1;
int head[N],ver[M],nex[M], tot = 1;
void addEdge(int x,int y){
	ver[++tot] = y; nex[tot] = head[x]; head[x] = tot;
}
int n,m;
int dfn[N],clk,low[N],co[N],col;
int Stack[N],top,deg[N];
void Tarjan(int x,int e){
	/* 对双连通分量进行染色、缩点 */
	dfn[x] = low[x] = ++clk;
	Stack[++top] = x;
	for(int i = head[x];i ;i = nex[i]){
		int y = ver[i];
		if(!dfn[y]){
			Tarjan(y,i); 
			low[x] = min(low[x],low[y]);
			//if(low[y] > dfn[x]) bridge[i] = bridge[i^1] = true;
		}else if((i^1) != e) low[x] = min(low[x],dfn[y]);
	}
	if(dfn[x] == low[x]) 
		for(++col;Stack[top+1] != x;--top)
			co[Stack[top]] = col;
}
bool vis[N];
void solve(){
	Tarjan(1,0);
	for(int x = 1;x <= n;x++)
		for(int i = head[x];i ;i = nex[i]){
			int y = ver[i]; vis[i] = true;
			if(!vis[i^1] && co[x] != co[y]) deg[co[x]]++,deg[co[y]]++;
		}
	int leaf = 0;
	for(int i = 1;i <= col;i++) if(deg[i] == 1) leaf++;
	printf("%d\n",leaf+1>>1);
}
int main(){
	scanf("%d%d",&n,&m);
	for(int i = 1,x,y;i <= m;i++){
		scanf("%d%d",&x,&y);
		addEdge(x,y), addEdge(y,x);
	}
	solve();
	return 0;
}
