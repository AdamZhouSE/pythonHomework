#include <bits/stdc++.h>
#define N 1000010
#define ll long long
using namespace std;

ll n, m, ans, tot, f[N];

struct edge {
    ll u, v, w;
    edge(ll u, ll v, ll w) : u(u), v(v), w(w) {}
};

vector<edge> e;

inline bool cmp(const edge& x, const edge& y) { return x.w < y.w; }

inline void init() {
    for (register int i = 1; i <= n; ++i) f[i] = i;
}

inline ll anc(ll x) {
    if (f[x] == x)
        return x;
    return f[x] = anc(f[x]);
}

inline void merge(int x, int y) {
    x = anc(x), y = anc(y);
    if (x != y)
        f[x] = y;
}

int main() {
    scanf("%lld%lld", &n, &m);
    init();
    for (register ll i = 0, u, v, w; i < m; ++i) {
        scanf("%lld%lld%lld", &u, &v, &w);
        e.push_back(edge(u, v, w));
    }
    sort(e.begin(), e.end(), cmp);
    for (register ll i = 0; i < m; ++i) {
        int x = anc(e[i].u), y = anc(e[i].v);
        if (x != y)
            merge(x, y), ans += e[i].w, ++tot;
        if (tot == n - 1)
            break;
    }
    printf("%lld", ans);
    return 0;
}