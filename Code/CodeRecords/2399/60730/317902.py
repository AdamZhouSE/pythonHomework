#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <list>
#include <map>
using namespace std;
#define ll long long
#define mod 998244353
ll MAXN = 1e7 + 2e5, sum1[200005], sum2[200005], f[20000005], ans, xinyue, n, m, l, r, val[200005], _m;
ll ksm(ll x, ll y) {
    ll anss = 1, t = x;
    while (y) {
        if (y & 1)
            anss = anss * t % mod;
        t = t * t % mod;
        y >>= 1;
    }
    return anss;
}
int main() {
    scanf("%lld", &xinyue);
    f[0] = 1;
    for (ll i = 1; i <= MAXN; i++) f[i] = f[i - 1] * i % mod;
    while (xinyue--) {
        scanf("%lld%lld%lld%lld", &n, &m, &l, &r);
        int _m = m;
        for (ll i = 1; i <= n; i++) {
            scanf("%lld", &val[i]);
        }
        sort(val + 1, val + n + 1);
        ll now = 0, num = 0;
        sum2[0] = r - l + 1;
        for (ll i = 1; i <= n; i++) {
            if (val[i] != now) {
                if (i != 1) {
                    if (now > r || now < l)
                        sum1[num]++;
                    else
                        sum2[num]++, sum2[0]--;
                }
                now = val[i];
                num = 1;
            } else if (val[i] == now)
                num++;
        }
        if (now > r || now < l)
            sum1[num]++;
        else
            sum2[num]++, sum2[0]--;
        now = 0;
        ans = 1;
        while (m >= sum2[now] && now < n) {
            sum2[now + 1] += sum2[now];
            m -= sum2[now];
            sum2[now] = 0;
            now++;
        }
        if (now == n) {
            num = sum2[now];
            now += m / num;
            //			cout<<now<<endl;
            m %= num;
            ans = ans * ksm(f[now + 1], m) % mod * ksm(f[now], num - m) % mod;
        } else {
            sum2[now + 1] += m;
            sum2[now] -= m;
            for (ll i = 1; i <= n; i++) {
                ans = ans * ksm(f[i], sum2[i]) % mod;
            }
        }
        for (ll i = 1; i <= n; i++) {
            for (ll t = 1; t <= sum1[i]; t++) {
                ans = ans * f[i] % mod;
            }
        }
        //		cout<<ans<<' '<<f[n+_m]<<endl;
        ans = ksm(ans, mod - 2);
        printf("%lld\n", f[n + _m] * ans % mod);
        for (ll i = 0; i <= n; i++) {
            sum1[i] = sum2[i] = 0;
        }
    }
}