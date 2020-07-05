
#include<vector>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define MAXN 6005
int h[MAXN];
int v[MAXN];
vector<int> son[MAXN];
int f[MAXN][2];
void dp(int x)
{
	f[x][0] = 0;
	f[x][1] = h[x];
	for (int i = 0; i < son[x].size(); i++)
	{
		int y = son[x][i];
		dp(y);
		f[x][0] += max(f[y][0], f[y][1]);
		f[x][1] += f[y][0];
	}
}
int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> h[i];
	for (int i = 1; i <= n - 1; i++)
	{
		int x, y;
		cin >> x >> y;
		son[y].push_back(x);
		v[x] = 1;
	}
	int root;
	for (int i = 1; i <= n; i++)
		if (!v[i]) { root = i; break; }
	dp(root);
	cout << max(f[root][0], f[root][1]) << "";
	return 0;
}