/*
 * File Name:	4251.cpp
 * Author	:	CraZYali
 * Time		:	2020.01.25 18:05
 * Email	:	yms-chenziyang@outlook.com
 */

#define DEP(i, s, e) for (register int i(s), end_##i(e); i >= end_##i; i--)
#define REP(i, s, e) for (register int i(s), end_##i(e); i <= end_##i; i++)
#define DEBUG fprintf(stderr, "Passing [%s] in Line %d\n", __FUNCTION__, __LINE__)

#define chkmax(a, b) (a < (b) ? a = (b) : a)
#define chkmin(a, b) (a > (b) ? a = (b) : a)

#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;
const int maxn = 250 + 5, maxm = 250 + 5, inf = 1e8;

namespace Graph {
int n, S, T;
const int maxn = 1e6, maxm = 1e6;
int bg[maxn], ne[maxm], to[maxm], w[maxm], e = 1;
void add(int x, int y, int z) {
    e++;
    to[e] = y;
    ne[e] = bg[x];
    bg[x] = e;
    w[e] = z;
}
void Add(int x, int y, int z = 1) {
    add(x, y, z);
    add(y, x, 0);
}
void init() {
    e = 1;
    REP(i, 1, n) bg[i] = 0;
}
int q[maxn], head, tail, dis[maxn];
bool bfs() {
    REP(i, 1, n) dis[i] = -1;
    dis[q[head = tail = 0] = T] = 0;
    while (head <= tail) {
        int x = q[head++];
        for (int i = bg[x]; i; i = ne[i])
            if (w[i ^ 1] > 0 && dis[to[i]] == -1) {
                dis[to[i]] = dis[x] + 1;
                q[++tail] = to[i];
            }
    }
    return dis[S] != -1;
}
int cur[maxn];
int dfs(int x, int y = inf) {
    if (x == T || !y)
        return y;
    int res = 0;
    for (int &i = cur[x]; i; i = ne[i])
        if (w[i] > 0 && dis[to[i]] == dis[x] - 1) {
            int tmp = dfs(to[i], min(y, w[i]));
            if (tmp > 0) {
                res += tmp;
                w[i] -= tmp;
                w[i ^ 1] += tmp;
                y -= tmp;
                if (!y)
                    break;
            }
        }
    return res;
}
void output() {
    REP(x, 1, n)
    for (int i = bg[x]; i; i = ne[i]) printf("%d %d %d\n", x, to[i], w[i]);
}
int Dinic() {
    int res = 0;
    while (bfs()) {
        copy(bg, bg + 1 + n, cur);
        while (1) {
            int tmp = dfs(S);
            if (!tmp)
                break;
            res += tmp;
        }
    }
    return res;
}
}  // namespace Graph

template <typename T>
inline T read() {
    T ans(0), flag(1);
    char c(getchar());
    while (!isdigit(c)) {
        if (c == '-')
            flag = -1;
        c = getchar();
    }
    while (isdigit(c)) {
        ans = ans * 10 + c - 48;
        c = getchar();
    }
    return ans * flag;
}

#define file(FILE_NAME) freopen(FILE_NAME ".in", "r", stdin), freopen(FILE_NAME ".out", "w", stdout);

int n, m, k, a[maxn][maxm], b[maxn * maxn], _;
bool judge(int val) {
    Graph::init();
    REP(i, 1, n)
    REP(j, 1, m)
    if (a[i][j] <= val)
        Graph::Add(i, j + n);
    REP(i, 1, n) Graph::Add(Graph::S, i);
    REP(i, 1, m) Graph::Add(i + n, Graph::T);
    return Graph::Dinic() >= n - k + 1;
}
int main() {
#ifdef CraZYali
    file("4251");
#endif
    n = read<int>();
    m = read<int>();
    Graph::n = n + m + 2;
    Graph::S = n + m + 1;
    Graph::T = n + m + 2;
    k = read<int>();
    REP(i, 1, n)
    REP(j, 1, m) {
        a[i][j] = read<int>();
        b[++_] = a[i][j];
    }
    sort(b + 1, b + 1 + _);
    _ = unique(b + 1, b + 1 + _) - b - 1;
    int l = 1, r = _;
    while (l <= r) {
        int mid = l + r >> 1;
        if (judge(b[mid]))
            r = mid - 1;
        else
            l = mid + 1;
    }
    cout << b[r + 1] << endl;
    return 0;
}