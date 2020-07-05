#include <cstdio>
#include <algorithm>
#define rep(i, x, y) for (int i = x; i <= y; ++i)

using namespace std;
const int N = 50, inf = 0x3f3f3f3f;
int tc, n, t, ans, a[N], l[N], r[N], flag[N];

void dfs(int x, int d) {
    if (d >= ans)
        return;
    if (x > t)
        return ans = d, void();
    for (flag[x] = 0; flag[x] < 2; ++flag[x]) {
        static int cnt[2];
        cnt[0] = cnt[1] = 0;
        rep(i, 1, x - 1) r[i] > l[x] ? ++cnt[flag[i] == flag[x] && r[i] < r[x]] : 0;
        dfs(x + 1, d + min(cnt[0], cnt[1]));
    }
}

void work() {
    scanf("%d", &n), t = 0;
    rep(i, 1, n) scanf("%d", a + i);
    rep(i, 1, n) rep(j, i + 1, n) if (a[i] == a[j])++ t, l[t] = i, r[t] = j;
    ans = inf, dfs(1, 0);
    printf("%d\n", ans);
}

int main() {
    for (scanf("%d", &tc); tc--; work())
        ;
    return 0;
}