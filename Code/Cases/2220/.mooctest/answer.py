#include <cstdio>
#include <algorithm>
using namespace std;
const int mod = 998244353;
int n, m, g[20][20], fa[21], inv[21], a[1 << 20 | 1][21], ans;
int find(int x) { return x == fa[x] ? x : fa[x] = find(fa[x]); }
int calc(int s) {
    int res = 1;
    for (int i = 0; i < n; ++i) fa[i] = i;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if ((s >> i & 1) && (s >> j & 1) && g[i][j]) {
                int x = find(i), y = find(j);
                if (x != y)
                    fa[x] = y;
                else
                    res = (res + res) % mod;
            }
    return res;
}
void Get_ln(int *f) {
    static int g[21];
    g[0] = 0;
    for (int i = 1; i <= n; ++i) {
        g[i] = 0;
        for (int j = 1; j < i; ++j) g[i] = (g[i] + 1ll * f[j] * g[i - j] % mod * (i - j)) % mod;
        g[i] = (f[i] - 1ll * inv[i] * (g[i] + mod) % mod + mod) % mod;
    }
    for (int i = 0; i <= n; i++) f[i] = g[i];
}
int main() {
    scanf("%d%d", &n, &m);
    inv[1] = 1;
    for (int i = 2; i <= n; ++i) inv[i] = 1ll * inv[mod % i] * (mod - mod / i) % mod;
    for (int i = 1, x, y; i <= m; ++i) {
        scanf("%d%d", &x, &y);
        --x;
        --y;
        g[x][y] = g[y][x] = 1;
    }
    for (int i = 0; i < 1 << n; ++i) a[i][__builtin_popcount(i)] = calc(i);
    for (int j = 1; j < 1 << n; j <<= 1)
        for (int i = 0; i < 1 << n; ++i)
            if (i & j)
                for (int k = 0; k <= n; ++k) a[i][k] = (a[i][k] + a[i ^ j][k]) % mod;
    for (int i = 0; i < 1 << n; ++i) {
        Get_ln(a[i]);
        if (__builtin_parity(((1 << n) - 1) ^ i))
            ans = (ans - a[i][n] + mod) % mod;
        else
            ans = (ans + a[i][n]) % mod;
    }
    printf("%d\n", ans);
    return 0;
}