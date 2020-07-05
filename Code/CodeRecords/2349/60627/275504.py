#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <algorithm>
#define R register
#define IN inline
#define W while
#define gc getchar()
#define MX 1200500
#define ll long long
template <class T>
IN void in(T &x)
{
	static bool neg; static char c;
	x = 0; c = gc;
	for (; !isdigit(c); c = gc)
	if (c == '-') neg = true;
	for (;  isdigit(c); c = gc)
	x = (x << 1) + (x << 3) + c - 48;
	if (neg) neg = false, x = -x;
}
int n, m, plcnt, q, cnt = -1, root;
ll ans1, ans2;
struct Point {int x, y;} dot[MX];
IN Point operator + (const Point &x, const Point &y)
{return {x.x + y.x, x.y + y.y};}
IN Point operator - (const Point &x, const Point &y)
{return {x.x - y.x, x.y - y.y};}
IN ll operator * (const Point &x, const Point &y)
{return 1ll * x.x * y.y - 1ll * x.y * y.x;}
struct Edge
{
	int x, y, id;
	double rat;
	Edge (){};
	Edge (R int fr, R int to, R int ID = 0)
	{
		x = fr, y = to, id = ID;
		rat = std::atan2(dot[to].y - dot[fr].y, dot[to].x - dot[fr].x);
	}
}edge[MX];
std::vector <Edge> g[MX], h[MX];
IN bool operator < (const Edge &x, const Edge &y) {return x.rat < y.rat;}
ll area[MX], area2[MX];
bool vis[MX], on[MX];
int bel[MX], nex[MX], fat[MX], que[MX];
IN int find(R int pos, const Edge &tar)
{return std::lower_bound(g[pos].begin(), g[pos].end(), tar) - g[pos].begin();}
void Build()
{	
	int st, tmp;
	for (R int i = 0; i <= cnt; ++i)
	{
		if (bel[i]) continue;
		st = edge[i].x, bel[i] = ++plcnt; tmp = i;
		W (2333)
		{
			tmp = nex[tmp];
			bel[tmp] = plcnt;
			if (edge[tmp].y == st) break;
			area[plcnt] += (dot[edge[tmp].x] - dot[st]) * (dot[edge[tmp].y] - dot[st]);
		}
		if (area[plcnt] <= 0) root = plcnt;
		area2[plcnt] = area[plcnt] * area[plcnt];
	}
	for (R int i = 0; i <= cnt; ++i)
	h[bel[i]].push_back(Edge(bel[i], bel[i ^ 1], i));
}
void DFS(R int now)
{
	vis[now] = true;
	for (R int i = h[now].size() - 1; ~i; --i)
	{
		if (vis[h[now][i].y]) continue;
		fat[h[now][i].y] = now; on[h[now][i].id] = on[h[now][i].id ^ 1] = true;
		DFS(h[now][i].y); area[now] += area[h[now][i].y];
		area2[now] += area2[h[now][i].y];
	}
}
int main(void)
{
	freopen("mine1.in", "r", stdin);
	freopen("my.out", "w", stdout);
	int foo, bar, now, oth;
	in(n), in(m), in(q);
	for (R int i = 1; i <= n; ++i)
	in(dot[i].x), in(dot[i].y);
	for (R int i = 1; i <= m; ++i)
	{
		in(foo), in(bar);
		++cnt;
		edge[cnt] = Edge(foo, bar, cnt);
		g[foo].push_back(edge[cnt]);
		++cnt;
		edge[cnt] = Edge(bar, foo, cnt);
		g[bar].push_back(edge[cnt]);
	}
	for (R int i = 1; i <= n; ++i) std::sort(g[i].begin(), g[i].end());
	for (R int i = 0; i <= cnt; ++i)
	{
		foo = find(edge[i].y, edge[i ^ 1]) - 1;
		if (foo < 0) foo = g[edge[i].y].size() - 1;
		nex[i] = g[edge[i].y][foo].id;
	}
	Build();
	DFS(root);
	W (q--)
	{
		in(foo);
		foo = (foo + ans1) % n + 1;
		for (R int i = 1; i <= foo; ++i) in(que[i]), que[i] = (que[i] + ans1) % n + 1;
		ans1 = ans2 = 0; que[foo + 1] = que[1];
		for (R int i = 1; i <= foo; ++i)
		{
			bar = find(que[i], Edge(que[i], que[i + 1]));
			bar = g[que[i]][bar].id;
			if (!on[bar]) continue;
			now = bel[bar], oth = bel[bar ^ 1];
			if (fat[oth] == now) ans1 -= area2[oth], ans2 -= area[oth];
			else ans1 += area2[now], ans2 += area[now];
		}
		if (ans1 < 0) ans1 = -ans1, ans2 = -ans2;
		ans2 *= 2;
		ll g = std::__gcd(ans1, ans2);
		printf("%lld %lld\n", ans1 /= g, ans2 /= g);
	}
}
