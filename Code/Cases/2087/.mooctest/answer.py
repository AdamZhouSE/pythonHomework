#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 250010
#define ll long long
struct Edge {
    int v, nx;
} e[MAXN << 1];
int head[MAXN], ecnt, mch[MAXN], n, x, y, tp1, tp2, ans;
bool vis[510];
ll a[MAXN], _[MAXN], __[MAXN];
template <typename T>
T gcd(T a, T b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}
void add(int f, int t) {
    e[++ecnt] = (Edge){ t, head[f] };
    head[f] = ecnt;
}
bool hungary(int u) {
    for (int i = head[u]; i; i = e[i].nx) {
        int to = e[i].v;
        if (!vis[to]) {
            vis[to] = 1;
            if (!mch[to] || hungary(mch[to])) {
                mch[to] = u;
                return 1;
            }
        }
    }
    return 0;
}
int main() {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%lld", &a[i]);
        if (a[i] & 1) {
            _[++tp1] = i;
        } else {
            __[++tp2] = i;
        }
    }
    for (int i = 1; i <= tp1; i++) {
        for (int j = 1; j <= tp2; j++) {
            if (gcd(a[_[i]], a[__[j]]) == 1 && gcd(a[_[i]] + 1, a[__[j]] + 1) == 1) {
                add(_[i], __[j]);
                // add(__[j], _[i]);
            }
        }
    }
    for (int i = 1; i <= tp1; i++) {
        memset(vis, 0, sizeof(vis));
        if (hungary(_[i])) {
            ans++;
        }
    }
    printf("%d", n - ans);
}