# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int mod(1e9 + 7);
const int inv2((mod + 1) >> 1);
const int inv3((mod + 1) / 3);
const int rt3(82062379);

inline int Pow(ll x, int y) {
    ll ret = 1;
    for (; y; y >>= 1, x = x * x % mod)
        if (y & 1) ret = ret * x % mod;
    return ret;
}

inline void Inc(int &x, int y) {
    x = x + y >= mod ? x + y - mod : x + y;
}

inline void Dec(int &x, int y) {
    x = x - y < 0 ? x - y + mod : x - y;
}

inline int Add(int x, int y) {
    return x + y >= mod ? x + y - mod : x + y;
}

inline int Sub(int x, int y) {
    return x - y < 0 ? x - y + mod : x - y;
}

struct Complex {
    int a, b;

    inline Complex(int _a = 0, int _b = 0) {
        a = _a, b = _b;
    }

    inline Complex operator +(Complex y) const {
        return Complex(Add(a, y.a), Add(b, y.b));
    }

    inline Complex operator -(Complex y) const {
        return Complex(Sub(a, y.a), Sub(b, y.b));
    }

    inline Complex operator *(Complex y) const {
        return Complex(Sub((ll)a * y.a % mod, (ll)b * y.b % mod), Add((ll)a * y.b % mod, (ll)b * y.a % mod));
    }

    inline Complex operator *(int y) const {
        return Complex((ll)a * y % mod, (ll)b * y % mod);
    }

    inline Complex operator /(int y) const {
        int inv = Pow(y, mod - 2);
        return Complex((ll)a * inv % mod, (ll)b * inv % mod);
    }

    inline Complex operator /(Complex y) const {
        return Complex(a, b) * Complex(y.a, mod - y.b) / Add((ll)y.a * y.a % mod, (ll)y.b * y.b % mod);
    }
} a[105][105], coef[3], inv, w[3], invw[3];

int n, m, eu[105 * 105], ev[105 * 105], ec[105 * 105], bin[20];

inline Complex Det() {
    int i, j, k;
    Complex ret = Complex(1, 0);
    for (i = 1; i < n; ++i) {
        for (j = i; j < n; ++j)
            if (a[j][i].a || a[j][i].b) {
                if (i == j) break;
                swap(a[i], a[j]), ret = ret * (mod - 1);
                break;
            }
        for (j = i + 1; j < n; ++j) {
            inv = a[j][i] / a[i][i];
            for (k = i; k < n; ++k) a[j][k] = a[j][k] - inv * a[i][k];
        }
        ret = ret * a[i][i];
    }
    return ret;
}

inline void IDFT(Complex *p) {
    int i;
    Complex tmp[3];
    tmp[0] = p[0], tmp[1] = p[1], tmp[2] = p[2];
    p[0] = tmp[0] + tmp[1] + tmp[2];
    p[1] = tmp[0] + tmp[1] * invw[1] + tmp[2] * invw[2];
    p[2] = tmp[0] + tmp[1] * invw[2] + tmp[2] * invw[1];
    for (i = 0; i < 3; ++i) p[i] = p[i] * inv3;
}

inline int Calc(int p) {
    int i, j, k;
    Complex w0, w1, w2, c;
    for (i = 0; i < 3; ++i) {
        memset(a, 0, sizeof(a));
        w0 = Complex(1, 0), w1 = w[i], w2 = w[(i + i) % 3];
        for (j = 1; j <= m; ++j) {
            k = ec[j] / bin[p] % 3;
            c = (k == 1 ? w1 : (k == 2 ? w2 : w0));
            a[eu[j]][eu[j]] = a[eu[j]][eu[j]] + c;
            a[ev[j]][ev[j]] = a[ev[j]][ev[j]] + c;
            a[eu[j]][ev[j]] = a[eu[j]][ev[j]] - c;
            a[ev[j]][eu[j]] = a[ev[j]][eu[j]] - c;
        }
        coef[i] = Det();
    }
    IDFT(coef);
    return (ll)Add(coef[1].a, Add(coef[2].a, coef[2].a)) * bin[p] % mod;
}

int main() {
    int i, ans = 0;
    scanf("%d%d", &n, &m);
    w[0] = Complex(1, 0), w[1] = Complex(mod - inv2, (ll)rt3 * inv2 % mod);
    w[2] = Complex(mod - inv2, mod - (ll)rt3 * inv2 % mod);
    invw[0] = Complex(1, 0) / w[0], invw[1] = Complex(1, 0) / w[1], invw[2] = Complex(1, 0) / w[2];
    for (i = 1; i <= m; ++i) scanf("%d%d%d", &eu[i], &ev[i], &ec[i]);
    for (bin[0] = i = 1; i <= 10; ++i) bin[i] = bin[i - 1] * 3;
    for (i = 0; i <= 10; ++i) Inc(ans, Calc(i));
    printf("%d\n", ans);
    return 0;
}