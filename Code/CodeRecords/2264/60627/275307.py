#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<unordered_map>
#include<set>
#include<sstream>
using namespace std;
const int MAXN = 505; 
 
vector<int> adj[MAXN];
long long t,n;
long long u,v;
long long cnt = 1;
/*
** low数组，假设low[v] = 5;
** 说明从v节点出发，能到达第五次Tarjan递归时的点，
** 假设第五次是对w节点进行的递归，也就说明v节点能够达到w节点。 
** 注意点：并不是说v只能到达w，可能w还能到达z节点，
** 也就是说v其实也能到达z节点。 
*/
int low[MAXN];  //Low[u]为u或u的子树能够追溯到的最早的Tarjan次序号。 
int dfn[MAXN];  //初始值都为0，表示还未访问，即：还未递归。 
int cut[MAXN];  //cut[u]=true 表示u是割点。 
long long index;  //记录当前Tarjan递归的次数。（不是层数，是次数） 
long long root;  //记录Tarjan的入口节点，也就是根节点。 
long long childNum;   //根节点对应的子节点的数量 
void Tarjan(int u,int parent){
	dfn[u] = low[u] = ++index;
	for(int i=0;i<adj[u].size();i++){
		int v = adj[u][i];
		if(!dfn[v]){   //如果v节点还没有访问过 
			Tarjan(v,u);
			low[u] = min(low[u],low[v]); 
			//判断割点啦 
			//满足第二个条件，v没有通向u父亲节点或祖宗节点的路线。
			//此时u一旦去除，v以及v的子节点就孤立了，所以u是割点。 
			if(low[v] >= dfn[u]){ 
				//满足第一个条件，u是根节点 
				if(u == root){
					childNum++; 
					//如果子节点已经大于等于两个了，它就是割点。 
					if(childNum>=2){
						cut[u] = true;
					}
				}else{
					cut[u] = true;
				} 
			}
		}else if(v != parent){
			low[u] = min(low[u],dfn[v]);
		}
	}
}
 
int vis[MAXN]; //vis[u] = 1  表示u节点属于第一个双连通分量 
long long cutNum;  //当前双连通分量连接着的割点数 
long long totalNum; //当前双连通分量共有多少个点（割点除外） 
long long out; //总共需要设置多少个出口。 
long long plan; //有多少种方案 
long long group; 
/*
** 查看当前的双连通分量连接着几个割点。
** 割点会把原来的连通分量划分为
** 若干个双连通分量，我们就是要看看
** 每一个双连通分量在原来的连通分量中
** 连接着几个割点。 
*/
void DFS(int u){
	vis[u] = group;
	totalNum++; 
	for(int i=0;i<adj[u].size();i++){
		int v = adj[u][i];
		/*
		**u是割点并且没有被这个双连通分量访问过，
		**因为一个割点可能连接多个双连通分量 
		**/ 
		if(cut[v] && vis[v]!=group){ 
			cutNum++; //双连通分量的割点+1 
			vis[v] = group;
		}
		if(!vis[v]){ //如果不是割点并且没有没访问过 
			DFS(v);
		}
	} 
}
 
void DFSTravel(){
	for(int i=1;i<=n;i++){
		if(!vis[i] && !cut[i]){ //不能是已访问过的点，也不能是割点 
			cutNum = 0;  //重置cutNum的值。 
			totalNum = 0;  
			group++;
			DFS(i);
			if(cutNum == 0){ 
				out += 2;
				plan *= totalNum*(totalNum-1)/2;
			}else if(cutNum == 1){
				out++;
				plan *= totalNum;
			}
			//如果cutNum==2，不用设置出口。 
		}
	}
}
 
void TarjanTravel(){
	for(int i=1;i<=n;i++){
		if(!dfn[i]){
			childNum = 0; //重置子节点数量的值。 
			root = i; 
			Tarjan(i,i);
		}
	}
}
 
void init_data(){
	//设置初值 
	fill(cut,cut+n+1,false);
	fill(dfn,dfn+n+1,0);
	fill(vis,vis+n+1,0);
	index = 0;
	plan = 1; 
	out = 0; 
	group = 0; //当前双连通分量的序号 
}
 
void destroy(){
	for(int i=1;i<MAXN;i++){
		adj[i].clear();
	}
	n = 0;
}
 
int main(){
	while(cin>>t && t!=0){
		for(int i=0;i<t;i++){
			cin>>u>>v;
			adj[u].push_back(v);
			adj[v].push_back(u);
			n = max(n,max(u,v));
		}
		init_data();
		TarjanTravel();
		DFSTravel(); 
		destroy();
		cout<<"Case "<<cnt<<": "<<out<<" "<<plan<<endl; 
		cnt++;
	}
	return 0; 
} 