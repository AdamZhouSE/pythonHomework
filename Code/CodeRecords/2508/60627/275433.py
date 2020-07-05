#include <iostream>
#include <vector>
 
#define SIZE 110
 
using namespace std;
 
struct edge
{
	int to, cap;
};
 
vector<edge> graph[SIZE];
int dp[SIZE][SIZE], m; // DP[I][J]表示第I个节点和它的子树保留J个树枝剩余苹果的最大值.
 
int dfs(int u, int pre) // DP过程
{
	int i, j, k, v, w, childcount = 0;
	
	for (i = 0; i < graph[u].size(); ++i)
	{
		v = graph[u][i].to;
		if (v == pre) // 确保不是回到了前一个点
		{
			continue;
		}
		w = graph[u][i].cap;
		childcount += dfs(v, u) + 1;
		for (j = min(childcount, m); j >= 1; --j)
		{
			for (k = min(j, childcount); k >= 1; --k)
			{
				dp[u][j] = max(dp[u][j], dp[u][j-k] + dp[v][k-1] + w); // 条件转移方程
			}
		}
	}
	
	return childcount; // 顺便返回二子数
}
 
int main(int argc, char** argv)
{
	int n, u, v, w, i;
	
	scanf("%d%d", &n, &m);
	for (i = 1; i < n; ++i)
	{
		scanf("%d%d%d", &u, &v, &w);
		graph[u].push_back({v, w}); // 建图
		graph[v].push_back({u, w});
	}
	
	dfs(1, -1);
	
	printf("%d", dp[1][m]);
		
	return 0;
}