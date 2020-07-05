#include<iostream>
#include<string.h>
using namespace std;
const int N = 1e4 + 5;
int dis[N], head[N], cnt;

struct road
{
	int to, nextNeighbor;
}e[N * 50];

void add(int x, int y)
{
	e[++cnt].to = y;
	e[cnt].nextNeighbor = head[x];
	head[x] = cnt;
}

void dfs(int x, int step)
{
	if (dis[x] != 0) return;
	dis[x] = step;
	for (int i = head[x]; i; i = e[i].nextNeighbor)
		dfs(e[i].to, step + 1);
}

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n-1; i++)
	{
		int x, y;
		cin >> x >> y;
		add(x, y);
		add(y, x);
	}

	dfs(1, 1);
	int Max = 0, k;
	for (int i = 1; i <= n; i++)
		if (dis[i] > Max) Max = dis[i], k = i;
	memset(dis, 0, sizeof(dis));

	dfs(k, 1);
	for (int i = 1; i <= n; i++)
		if (dis[i] > Max) Max = dis[i];

	cout << Max - 1 << endl;
}