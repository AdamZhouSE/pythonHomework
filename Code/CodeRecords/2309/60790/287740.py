#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;

#define Fill_1(x) memset(x, -1, sizeof x)
#define transform(i, j) (i - 1) * m + j

const int N = 100000 + 1000;
const int M = 10 * N;
const int inf = 2147483647;

int n, m, NUM, ans = 0;
int Yuyuko = 0, Sanae = 0;
int F[N << 2], v[M << 2], nex[M << 2], w[M << 2], EID = 0;
int d[N << 2];
char str[2][N];

inline void add(int f, int t, int W)
{
	nex[EID] = F[f];
	v[EID] = t;
	w[EID] = W;
	F[f] = EID++;
}

inline bool bfs()
{
	Fill_1(d);
	d[Yuyuko] = 1;
	queue<int> q;
	q.push(Yuyuko);
	while(!q.empty())
	{
		int f = q.front();q.pop();
		for(int i = F[f];i != -1;i = nex[i])
		{
			if(d[v[i]] == -1 && w[i] > 0)
            {
                d[v[i]] = d[f] + 1;
                q.push(v[i]);
            }
        }
	}

	return d[Sanae] != -1;
}

inline int find(int x, int maxflow)
{
	if(x == Sanae)
		return maxflow;

	int ret = 0, flow = 0;

	for(int i = F[x];i != -1;i = nex[i])
		if(d[v[i]] == d[x] + 1 && w[i] > 0 && (flow = find(v[i], min(w[i], maxflow))))
		{
			w[i] -= flow;
			w[i ^ 1] += flow;
			maxflow -= flow;
			ret += flow;
			if(maxflow == 0)
				return ret;
		}

	return ret;
}

inline int dinic()
{
	int flow = 0, ret = 0;
	while(bfs())
		while(flow = find(Yuyuko, inf))
			ret += flow;
	return ret;
}

int main()
{
	Fill_1(F);
	Fill_1(nex);
	scanf("%d %d", &n, &m);
	NUM = n * m;
	Yuyuko = NUM * 2 + 1, Sanae = NUM * 2 + 2;
	int cur;
	for(int T = 1;T <= n;++T)
	{
		cur = T & 1;
		scanf("%s", str[cur] + 1);
		for(int i = 1;i <= m;++i)
		{
			if(str[cur][i] == '*')
				continue;
			else if(str[cur][i] == '2')
				++ans;
			else if(str[cur][i] == '1')
			{
				add(Yuyuko, transform(T, i), 1);
				add(transform(T, i), Yuyuko, 0);
				if(T != 1 && str[cur ^ 1][i] == '3')
					add(transform(T, i), transform(T - 1, i), 1), add(transform(T - 1, i), transform(T, i), 0);
				if(i < m && str[cur][i + 1] == '3')
					add(transform(T, i), transform(T, i + 1), 1), add(transform(T, i + 1), transform(T, i), 0);
				if(i > 1 && str[cur][i - 1] == '3')
					add(transform(T, i), transform(T, i - 1), 1), add(transform(T, i - 1), transform(T, i), 0);
			}
			else if(str[cur][i] == '3')
			{
				add(transform(T, i), Sanae, 1);
				add(Sanae, transform(T, i), 0);
				if(T != 1 && str[cur ^ 1][i] == '1')
					add(transform(T - 1, i), transform(T, i), 1), add(transform(T, i), transform(T - 1, i), 0);
			}
		}
	}
	ans += dinic();
	printf("%d\n", ans);

	return 0;
}
