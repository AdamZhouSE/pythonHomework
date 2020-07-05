//#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
//#define LOCAL
const int maxn = 3e5+5, maxl = 21;
int n, a[maxn], cnt, head[maxn], fa[maxn][maxl], dep[maxn], b[maxn];
bool v[maxn];
struct Arc
{
	int from, to, nxt;
}g[maxn << 1];

void addarc(int from, int to)
{
	g[cnt].from = from, g[cnt].to = to, g[cnt].nxt = head[from];
	head[from] = cnt++;
}

void dfs(int cur)
{
	v[cur] = true;
	for (int h = head[cur], to; ~h; h = g[h].nxt)
	{
		to = g[h].to;
		if (v[to])
		{
			continue;
		}
		fa[to][0] = cur;
		dep[to] = dep[cur] + 1;
		dfs(to);
	}
}

int lca(int x, int y)
{
	if (dep[x] > dep[y])
	{
		swap(x, y);
	}
	for (int j = maxl - 1; ~j; j--)
	{
		if (dep[fa[y][j]] >= dep[x])
		{
			y = fa[y][j];
		}
	}
	if (x == y)
	{
		return x;
	}
	for (int j = maxl - 1; ~j; j--)
	{
		if (fa[x][j] ^ fa[y][j])
		{
			x = fa[x][j];
			y = fa[y][j];
		}
	}
	return fa[x][0];
}

void cf(int x, int y)
{
	int a = lca(x, y);
	++b[x];
	++b[y];
	--b[a];
	--b[fa[a][0]];
}

void dfs1(int cur)
{
	v[cur] = true;
	for (int h = head[cur], to; ~h; h = g[h].nxt)
	{
		to = g[h].to;
		if (v[to])
		{
			continue;
		}
		dfs1(to);
		b[cur] += b[to];
	}
}

int main()
{
#ifdef LOCAL
	freopen("d:\\data.in","r",stdin);
//	freopen("d:\\my.out", "w", stdout);
#endif
	memset(head, -1, sizeof(head));
	scanf("%d", &n);
	for (int i = 1; i<=n; i++)
	{
		scanf("%d", a + i);
	}
	int x, y;
	for (int i = 1;i < n; i++)
	{
		scanf("%d%d", &x, &y);
		addarc(x, y);
		addarc(y, x);
	}
	dep[1] = 1;
	dfs(1);
	for (int j = 1, pa; j < maxl; j++)
	{
		for (int i = 1; i <= n; i++)
		{
			pa = fa[i][j - 1];
			fa[i][j] = fa[pa][j - 1];
		}
	}
	for (int i = 1; i < n; i++)
	{
		x = a[i];
		y = a[i + 1];
		cf(x, y);
	}
	memset(v, 0, sizeof(v));
	dfs1(1);
	for (int i = 1; i <= n; i++)
	{
		if (i ^ a[1])
		{
			--b[i];
		}
		printf("%d\n", b[i]);
	}
	return 0;
}
