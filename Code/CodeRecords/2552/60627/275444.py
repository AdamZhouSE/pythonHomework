#include <bits/stdc++.h>
#define ll long long
#define INF 0x3f3f3f3f
#define MAX 100010
using namespace std;
ll n, m, w[MAX << 2], lz[MAX << 2], f, a, b, p[MAX << 2], lp[MAX << 2];
void up(ll rt) {
    w[rt] = w[rt << 1] + w[rt << 1 | 1];
}
void up1(ll rt) {
    p[rt] = p[rt << 1] + p[rt << 1 | 1];
}
void down1(ll rt, ll ln, ll rn) {
    if(lp[rt]) {
        lp[rt << 1] += lp[rt];
        lp[rt << 1 | 1] += lp[rt];
        p[rt << 1] += lp[rt] * ln;
        p[rt << 1 | 1] += lp[rt] * rn;
        lp[rt] = 0;
    }
}
void down(ll rt, ll ln, ll rn) {
    if(lz[rt]) {
        lz[rt << 1] += lz[rt];
        lz[rt << 1 | 1] += lz[rt];
        w[rt << 1] += lz[rt] * ln;
        w[rt << 1 | 1] += lz[rt] * rn;
        lz[rt] = 0;
    }
}
void update(ll L, ll R, ll C, ll l, ll r, ll rt) {
    if(L <= l && r <= R) {
        w[rt] += C * (r - l + 1);
        lz[rt] += C;
        return;
    }
    ll m = (r + l) >> 1;
    down(rt, m - l + 1, r - m);
    if(L <= m)
        update(L, R, C, l, m, rt << 1);
    if(R > m)
        update(L, R, C, m + 1, r, rt << 1 | 1);
    up(rt);
}
void update1(ll L, ll R, ll C, ll l, ll r, ll rt) {
    if(L <= l && r <= R) {
        p[rt] += C * (r - l + 1);
        lp[rt] += C;
        return;
    }
    ll m = (r + l) >> 1;
    down1(rt, m - l + 1, r - m);
    if(L <= m)
        update1(L, R, C, l, m, rt << 1);
    if(R > m)
        update1(L, R, C, m + 1, r, rt << 1 | 1);
    up1(rt);
}
ll query(ll L, ll R, ll l, ll r, ll rt) {
    if(L <= l && r <= R) {
        return w[rt];
    }
    ll m = (r + l) >> 1;
    down(rt, m - l + 1, r - m);
    ll ans = 0;
    if(L <= m)
        ans += query(L, R, l, m, rt << 1);
    if(R > m)
        ans += query(L, R, m + 1, r, rt << 1 | 1);
    return ans;
}
ll query1(ll L, ll R, ll l, ll r, ll rt) {
    if(L <= l && r <= R) {
        return p[rt];
    }
    ll m = (r + l) >> 1;
    down1(rt, m - l + 1, r - m);
    ll ans = 0;
    if(L <= m)
        ans += query1(L, R, l, m, rt << 1);
    if(R > m)
        ans += query1(L, R, m + 1, r, rt << 1 | 1);
    return ans;
}
int main() {
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        cin >> f;
        if(f == 1) {
            cin >> a >> b;
            update(a, a, 1, 1, n, 1);
            update1(b, b, 1, 1, n, 1);
        } else {
            cin >> a >> b;
            cout << query(1, b, 1, n, 1) - query1(1, a - 1, 1, n, 1) << endl;
        }
    }
    return 0;
}