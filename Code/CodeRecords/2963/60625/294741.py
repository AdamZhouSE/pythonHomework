#include <stdio.h>
#include <vector>
#include <queue>
#include <memory.h>
#include <algorithm>
#include <iostream>
#define H 19260817
#define lim 100
using namespace std;
int Last[500002], Next[1000002], End[1000002], Len[1000002];
long long ans = 0;
int s[500002], maxs[500002], vis[500002], n, cnt[1002][1002], tnc[500002];
struct dat {
	int s, t, d;
	dat() {}
	dat(int p, int q, int r) {
		s = p;
		t = q;
		d = r;
	}
};
struct node {
	node *s[2], *f, *Next, *Last;
	int cnt, d;
	bool mk;
	std::vector<dat> pre;
} tr[500002], *null = tr, *top = tr - 1, *rt;
std::queue<node *> q;
std::priority_queue<std::pair<int, std::pair<int, int> > > Q;
node *addnode(int d) {
	node *p = ++top;
	p->s[0] = p->s[1] = p->Next = p->Last = null;
	p->cnt = 0;
	p->d = d;
	p->pre.clear();
	p->mk = 0;
	return p;
}
void dfs(int p, int f, node *t) {
	t->cnt++;
	for (int i = Last[p]; i; i = Next[i])
		if (!vis[End[i]] && End[i] != f) {
			if (t->s[Len[i]] == null)
				t->s[Len[i]] = addnode(t->d + 1);
			dfs(End[i], p, t->s[Len[i]]);
		}
}
void dfs1(node *p, unsigned long long h1, unsigned long long h2, unsigned long long d) {
	if (h1 == h2 && p != rt) {
		int tmp;
		p->mk = 1;
		if (p->pre.empty())
			p->pre.push_back(dat(p->d, p->d, p->d));
		else if (p->pre.back().t + p->pre.back().d == p->d)
			p->pre.back().t = p->d;
		else
			tmp = p->pre.back().t, p->pre.push_back(dat(p->d, p->d, p->d - tmp));
	}
	if (p->s[0] != null)
		p->s[0]->pre = p->pre, dfs1(p->s[0], h1 % H, h2 * 47 % H, d * 47 % H);
	if (p->s[1] != null)
		p->s[1]->pre = p->pre, dfs1(p->s[1], (h1 + d) % H, (h2 * 47 + 1) % H, d * 47 % H);
}
void bfs() {
	while (!q.empty()) q.pop();
	q.push(rt);
	rt->f = rt;
	while (!q.empty()) {
		node *t = q.front();
		q.pop();
		if (t->f != t)
			t->Next = t->f->Last, t->f->Last = t;
		t->s[0] == null
			? (t->s[0] = t->f->s[0])
			: (q.push(t->s[0]), t->s[0]->f = t->f->s[0] == t->s[0] || t->f->s[0] == null ? rt : t->f->s[0]);
		t->s[1] == null
			? (t->s[1] = t->f->s[1])
			: (q.push(t->s[1]), t->s[1]->f = t->f->s[1] == t->s[1] || t->f->s[1] == null ? rt : t->f->s[1]);
	}
}
void dfs2(node *p, int mul, int g) {
	ans += 1ll * mul * (p->cnt - 1) * p->cnt / 2;
	for (int i = 1; i <= lim; i++) cnt[i][p->d % i] += p->cnt;
	tnc[p->d] += p->cnt;
	for (int i = 0; i < p->pre.size(); i++) {
		Q.push(std::make_pair(p->d - p->pre[i].s, std::make_pair(p->pre[i].d, p->cnt)));
		if (p->d - p->pre[i].t >= p->pre[i].d)
			Q.push(std::make_pair(p->d - p->pre[i].t - p->pre[i].d, std::make_pair(p->pre[i].d, -p->cnt)));
	}
	for (node *t = p->Last; t != null; t = t->Next) {
		dfs2(t, mul, g);
		while (!Q.empty() && Q.top().first >= p->d) {
			int g = Q.top().first, d = Q.top().second.first, m = Q.top().second.second;
			Q.pop();
			if (d <= lim)
				ans += 1ll * m * mul * cnt[d][g % d];
			else
				for (int t = g; t >= 0; t -= d) ans += 1ll * m * mul * tnc[t];
		}
	}
	for (int i = 1; i <= lim; i++) cnt[i][p->d % i] -= p->cnt;
	tnc[p->d] -= p->cnt;
}
void calc(int p, int e) {
	top = tr;
	if (!e) {
		rt = addnode(0);
		dfs(p, 0, rt);
		dfs1(rt, 0, 0, 1);
		bfs();
		dfs2(rt, 1, 1);
		return;
	}
	rt = addnode(0);
	rt->s[Len[e]] = addnode(1);
	dfs(End[e], p, rt->s[Len[e]]);
	dfs1(rt, 0, 0, 1);
	bfs();
	dfs2(rt, -1, 0);
}
void getsiz(int p, int f) {
	s[p] = 1;
	for (int i = Last[p]; i; i = Next[i])
		if (!vis[End[i]] && End[i] != f)
			getsiz(End[i], p), s[p] += s[End[i]];
}
int getg(int p, int f, int ts) {
	maxs[p] = ts - s[p];
	int g = 0;
	for (int i = Last[p]; i; i = Next[i])
		if (!vis[End[i]] && End[i] != f) {
			int q = getg(End[i], p, ts);
			if (maxs[q] < maxs[g])
				g = q;
			if (s[End[i]] > maxs[p])
				maxs[p] = s[End[i]];
		}
	return maxs[p] < maxs[g] ? p : g;
}
int getg(int p) {
	getsiz(p, 0);
	return getg(p, 0, s[p]);
}
void work(int p) {
	p = getg(p);
	calc(p, 0);
	for (int i = Last[p]; i; i = Next[i])
		if (!vis[End[i]])
			calc(p, i);
	vis[p] = 1;
	for (int i = Last[p]; i; i = Next[i])
		if (!vis[End[i]])
			work(End[i]);
}
int main() {
	scanf("%d", &n);
	addnode(0);
	maxs[0] = 1e9;
	for (int i = 1; i < n + n - 2; i += 2) {
		scanf("%d%d%d", &End[i + 1], &End[i], &Len[i]);
		Len[i + 1] = Len[i];
		Next[i] = Last[End[i + 1]];
		Last[End[i + 1]] = i;
		Next[i + 1] = Last[End[i]];
		Last[End[i]] = i + 1;
	}
	work(1);
	printf("%lld", ans);
	cout << endl;
}