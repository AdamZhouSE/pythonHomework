#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define Fast_IO ios::sync_with_stdio(false);
#define fir first
#define sec second
#define mod 998244353
inline int read() {
    char ch = getchar();
    int nega = 1;
    while (!isdigit(ch)) {
        if (ch == '-')
            nega = -1;
        ch = getchar();
    }
    int ans = 0;
    while (isdigit(ch)) {
        ans = ans * 10 + ch - 48;
        ch = getchar();
    }
    if (nega == -1)
        return -ans;
    return ans;
}
typedef pair<int, int> pii;
int add(int x, int y) { return x + y > mod ? x + y - mod : x + y; }
int sub(int x, int y) { return x - y < 0 ? x - y + mod : x - y; }
#define N 11000005
int fac[N], inv[N];
int a[N], b[N], c[N];
int qpow(int x, int y) {
    int ans = 1;
    while (y) {
        if (y & 1)
            ans = 1LL * ans * x % mod;
        x = 1LL * x * x % mod;
        y >>= 1;
    }
    return ans;
}
void work() {
    int n = read(), m = read(), l = read(), r = read();
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        a[i] = read();
        if (a[i] >= l && a[i] <= r)
            b[++cnt] = a[i];
    }
    sort(a + 1, a + n + 1);
    sort(b + 1, b + cnt + 1);
    int c2 = 0;
    for (int i = 1; i <= cnt; i++) {
        if (b[i] != b[i - 1])
            c2++, c[c2] = 0;
        c[c2]++;
    }
    //	cout<<c2<<endl;
    //	for(int i=1;i<=c2;i++) printf("%lld ",c[i]); cout<<'\n';
    int ans = fac[n + m];
    for (int i = 1; i <= n; i++) {
        if (a[i] >= l && a[i] <= r)
            continue;
        int j = i;
        while (a[j + 1] == a[i] && j < n) j++;
        ans = 1LL * ans * inv[j - i + 1] % mod;
        i = j;
    }
    sort(c + 1, c + c2 + 1);
    int tot = r - l + 1 - c2;
    for (int i = 1; i <= c2; i++) {
        if (tot + i - 1 == 0) {
            m += c[i];
            continue;
        }
        int cur = m / (tot + i - 1);
        if (cur <= c[i]) {
            int r = m % (tot + i - 1);
            ans = 1LL * ans * qpow(inv[cur + 1], r) % mod;
            ans = 1LL * ans * qpow(inv[cur], tot + i - 1 - r) % mod;
            for (int j = i; j <= c2; j++) ans = 1LL * ans * inv[c[j]] % mod;
            printf("%d\n", ans);
            return;
        }
        m += c[i];
    }
    tot = r - l + 1;
    int cur = m / (tot);
    int re = m % (tot);
    ans = 1LL * ans * qpow(inv[cur + 1], re) % mod;
    ans = 1LL * ans * qpow(inv[cur], tot - re) % mod;
    printf("%d\n", ans);
}
signed main() {
#ifdef __LOCAL__
    freopen("in.txt", "r", stdin);
#endif
    fac[0] = 1;
    for (int i = 1; i <= N - 5; i++) fac[i] = 1LL * fac[i - 1] * i % mod;
    inv[0] = inv[1] = 1;
    for (int i = 2; i <= N - 5; i++) inv[i] = 1LL * (mod - mod / i) * inv[mod % i] % mod;
    for (int i = 2; i <= N - 5; i++) inv[i] = 1LL * inv[i - 1] * inv[i] % mod;
    int T = read();
    while (T--) work();
#ifdef __LOCAL__
    cout << "Time Used : " << clock() << endl;
#endif
    return 0;
}