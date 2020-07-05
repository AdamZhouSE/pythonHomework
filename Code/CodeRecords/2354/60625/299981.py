#include <bits/stdc++.h>

typedef long long ll;
const int N = 1054, mod = 1000000007, pmod = mod - 1;

int R, C;
ll K;
char s[N][N];

inline int &reduce(int &x) { return x += x >> 31 & mod; }
inline ll &preduce(ll &x) { return x += x >> 63 & pmod; }
ll PowerMod(ll a, ll n, ll c = 1) {
    for (preduce(n %= pmod); n; n >>= 1, a = a * a % mod)
        if (n & 1)
            c = c * a % mod;
    return c;
}

int main() {
    int i, j, v, V = 0, r = 0, hor = 0, ver = 0, ans = 0;
    scanf("%d%d%lld", &R, &C, &K), --K;
    for (i = 0; i < R; ++i)
        for (scanf("%s", s[i]), j = 0; j < C; ++j) V += s[i][j] &= 1;
    for (i = 0; i < R; ++i) hor += s[i][0] && s[i][C - 1];
    for (j = 0; j < C; ++j) ver += s[0][j] && s[R - 1][j];
    if (hor && ver)
        return putchar(49), putchar(10), 0;
    if (!(hor || ver))
        return printf("%lld\n", PowerMod(V, K)), 0;
    v = hor + ver;
    for (i = 0; i < R; ++i)
        for (j = 0; j < C; ++j) r += s[i][j] && (hor ? s[i][j + 1] : s[i + 1][j]);
    ans = PowerMod(V - v, -1, r) * (PowerMod(V, K) - PowerMod(v, K)) % mod;
    printf("%d\n", reduce(ans = PowerMod(V, K) - ans));
    return 0;
}