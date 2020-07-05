#include <bits/stdc++.h>

#define For(i, l, r) for (register int i = (l), i##end = (int)(r); i <= i##end; ++i)
#define Fordown(i, r, l) for (register int i = (r), i##end = (int)(l); i >= i##end; --i)
#define Rep(i, r) for (register int i = (0), i##end = (int)(r); i < i##end; ++i)
#define Set(a, v) memset(a, v, sizeof(a))
#define Cpy(a, b) memcpy(a, b, sizeof(a))
#define debug(x) cout << #x << ": " << (x) << endl

using namespace std;

template<typename T> inline bool chkmin(T &a, T b) { return b < a ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, T b) { return b > a ? a = b, 1 : 0; }

inline int read() {
	int x(0), sgn(1); char ch(getchar());
	for (; !isdigit(ch); ch = getchar()) if (ch == '-') sgn = -1;
	for (; isdigit(ch); ch = getchar()) x = (x * 10) + (ch ^ 48);
	return x * sgn;
}

void File() {
#ifdef zjp_shadow
	freopen ("2268.in", "r", stdin);
	freopen ("2268.out", "w", stdout);
#endif
}

const int N = 40100, K = 500100, M = 5.5e7 + 10;

int n, m;

int dfn[2][N], lis[2][N], sz[N], clk; 

vector<int> G[N];

int w[N], c[N], sum[N];

void Dfs_Init(int u, int id) {
	sz[u] = 1; sum[u] += w[u];
	for (int v : G[u])
		sum[v] = sum[u], Dfs_Init(v, id), sz[u] += sz[v];
	lis[id][dfn[id][u] = ++ clk] = u;
}

#define dp(id, x, y) dp[id][(x) * (m + 1) + (y)]

int dp[2][M], val[K], que[K], fr, tl;

void Dp(int id) {
	For (i, 1, clk) {
		int u = lis[id][i];
		For (j, 0, m)
			dp(id, i, j) = dp(id, i - sz[u], j);

		fr = 1; tl = 0;
		For (j, 0, m) {
			while (fr <= tl && j - que[fr] > c[u]) ++ fr;
			if (fr <= tl)
				chkmax(dp(id, i, j), val[que[fr]] + j * w[u]);
			val[j] = dp(id, i - 1, j) - j * w[u];
			while (fr <= tl && val[que[tl]] <= val[j]) -- tl;
			que[++ tl] = j;
		}
	}
}

bool leaf[N]; int tot;

void Init() {
	Set(leaf, true);
	For (i, 1, n) G[i].clear();
}

int main () {

	File();

	int cases = read();

	while (cases --) {

		Init();

		tot = n = read(), m = read();

		int rt = 0;

		For (i, 1, n) {
			int fa = read();
			if (fa) {
				leaf[fa] = false;
				G[fa].push_back(i);
			} else rt = i;
			int ai = read(), vi = read(); w[i] = vi; c[i] = 1;

			if (ai > 1) {
				int id = ++ tot; 
				w[id] = vi; c[id] = ai - 1; G[i].push_back(id);
			}
		}

		Rep (id, 2) {
			sum[rt] = clk = 0, Dfs_Init(rt, id), Dp(id);
			For (i, 1, n) reverse(G[i].begin(), G[i].end());
			For (i, 1, n) For (j, 1, m)
				chkmax(dp(id, i, j), dp(id, i, j - 1));
		}

		int ans = 0;
		For (i, 1, n) if (leaf[i]) {
			For (j, 0, m)
				chkmax(ans, dp(0, dfn[0][i] - 1, j) + dp(1, dfn[1][i] - sz[i], m - j) + sum[i]);
		}

		For (i, 1, tot) For (j, 0, m) 
			dp(0, i, j) = dp(1, i, j) = 0;

		printf ("%d\n", ans);

	}

	return 0;

}