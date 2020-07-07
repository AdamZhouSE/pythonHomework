#include <cstdio>
#include <cctype>
#include <iostream>
#include <algorithm>
using namespace std;

const int N = 2 * 1e5 + 2, NN = 1002, lim = (1 << 30) - 1;
int n, m, q, ans[N], dp[NN][NN], pos;
struct ask {
    int l, r, s, t, id;
} s[N];
struct edge {
    int u, v;
} line[N];

bool cmp(const ask a, const ask b) { return a.l < b.l; }

int read() {
    int x = 0;
    char s = getchar();
    while (!isdigit(s)) s = getchar();
    while (isdigit(s)) {
        x = (x << 1) + (x << 3) + (s ^ 48);
        s = getchar();
    }
    return x;
}

int main() {
    n = read();
    m = read();
    q = read();
    for (int i = 1; i <= m; ++i) line[i] = (edge){ read(), read() };
    for (int i = 1; i <= q; ++i) s[i] = (ask){ read(), read(), read(), read(), i };
    sort(s + 1, s + q + 1, cmp);
    pos = q;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j) dp[i][j] = lim;
    for (int i = m; i >= 1; --i) {
        dp[line[i].u][line[i].v] = dp[line[i].v][line[i].u] = i;
        for (int j = 1; j <= n; ++j) {
            // dp[line[i].u][j] =
            dp[line[i].u][j] = min(dp[line[i].u][j], dp[line[i].v][j]);
            // dp[line[i].v][j] =
            dp[line[i].v][j] = min(dp[line[i].v][j], dp[line[i].u][j]);
        }
        while (s[pos].l == i) {
            ans[s[pos].id] = (dp[s[pos].s][s[pos].t] <= s[pos].r);
            --pos;
        }
    }
    for (int i = 1; i <= q; ++i) printf("%s\n", ans[i] ? "Yes" : "No");
    return 0;
}