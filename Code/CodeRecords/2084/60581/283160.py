#include<stdio.h>
#include<string.h>
 
#define N 3000
#define INF 0x3f3f3f3f
int e[N][N];
int dist[N];  ///起始点到各顶点i的距离
int visited[N];
int pre[N];  ///pre[i]=j,从j-->i
int n, m; ///顶点数，边数
int s, t; ///起点，终点
 
///初始化邻接矩阵
void init_e() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++)
			if (i == j) e[i][j] = 0;
			else e[i][j] = INF;
	}
}
 
void Dijkstra() {
	//memset(visited,0,sizeof(visited);
	///初始化dist和pre,起始点到各顶点i的距离
	for (int i = 1; i <= n; i++) {
		dist[i] = e[s][i];
		pre[i] = s; ///s-->i
	}
	visited[s] = 1;
	for (int i = 2; i <= n; i++) {
		int min = INF, u;
		for (int i = 1; i <= n; i++) {
			if (!visited[i] && dist[i] < min) {
				min = dist[i];
				u = i;
			}
		}
		visited[u] = 1;
		///遍历u的邻接顶点，更新dist
		for (int i = 1; i <= n; i++) {
			if (!visited[i] && dist[u] + e[u][i] < dist[i]) {
				dist[i] = dist[u] + e[u][i];
				pre[i] = u;
			}
		}
	}
	printf("%d\n", dist[t]);
 
}
 
///输出最短路径，递归
void search(int x){
	if(x==s){
		printf("%d",x );
		return;
	}
}
 
int main() {
	scanf("%d%d%d%d", &n, &m, &s, &t);
	init_e();
	int a, b, w;
	for (int i = 0; i < m; i++) {
		scanf("%d%d%d", &a, &b, &w);
		///邻接矩阵只能存两个顶点间的一条路，这儿处理题目中的注意事项
		///只存两个顶点间最小的那条路
		if (w < e[a][b]) {  
			e[a][b] = w;
			e[b][a] = w; ///无向图
		}
	}
	Dijkstra();
	search(t);  ///参数为终点
	return 0;
}